/**
 * 该文件可自行根据业务逻辑进行调整
 */
import { useAppConfig } from '@vben/hooks';
import { preferences } from '@vben/preferences';
import { errorMessageResponseInterceptor, RequestClient } from '@vben/request';
import { message } from 'ant-design-vue';
import type { AxiosError } from 'axios';

const { apiURL } = useAppConfig(import.meta.env, import.meta.env.PROD);

function createRequestClient(baseURL: string) {
  const client = new RequestClient({
    baseURL,
  });
  // 请求头处理
  client.addRequestInterceptor({
    fulfilled: async (config) => {
      config.headers['Accept-Language'] = preferences.app.locale;
      return config;
    },
  });
  // response数据解构
  client.addResponseInterceptor({
    fulfilled: (response) => {
      const { data: responseData, status } = response;

      if (status >= 200 && status < 400) {
        return responseData;
      }
      throw new Error(`Error ${status}`);
    },
  });

  // 通用的错误处理,如果没有进入上面的错误处理逻辑，就会进入这里
  client.addResponseInterceptor(
    errorMessageResponseInterceptor((msg: string) => message.error(msg)),
  );

  // 错误处理增强
  client.addResponseInterceptor({
    rejected: (error: AxiosError) => {
      if (error.response) {
        // 服务器响应了错误状态码
        message.error(`请求错误: ${error.response.status}`);
      } else if (error.request) {
        // 请求已经发出，但没有收到响应
        message.error('网络错误，请检查您的网络连接');
      } else {
        // 在设置请求时发生了一些事情，触发了错误
        message.error('请求配置错误');
      }
      return Promise.reject(error);
    },
  });

  return client;
}

export const requestClient = createRequestClient(apiURL);

export const baseRequestClient = new RequestClient({ baseURL: apiURL });
