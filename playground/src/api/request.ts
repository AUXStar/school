/**
 * 该文件可自行根据业务逻辑进行调整
 */
import { useAppConfig } from '@vben/hooks';
import { preferences } from '@vben/preferences';
import { errorMessageResponseInterceptor, RequestClient } from '@vben/request';

import { message } from 'ant-design-vue';

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

  return client;
}

export const requestClient = createRequestClient(apiURL);

export const baseRequestClient = new RequestClient({ baseURL: apiURL });
