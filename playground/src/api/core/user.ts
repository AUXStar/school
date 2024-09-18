import type { UserInfo } from '@vben/types';

import { baseRequestClient, requestClient } from '#/api/request';

export namespace AuthApi {
  /** 登录接口参数 */
  export interface LoginParams {
    password: string;
    username: string;
  }

  /** 登录接口返回值 */
  export interface LoginResult {
    id: number;
  }
}

/**
 * 登录
 */
export async function loginApi(data: AuthApi.LoginParams) {
  return requestClient.post<AuthApi.LoginResult>('/user/login', data);
}

/**
 * 退出登录
 */
export async function logoutApi() {
  return baseRequestClient.get('/user/logout');
}

/**
 * 获取用户个人信息
 */
export async function getUserSelfInfoApi() {
  return requestClient.get<UserInfo>('/user/self_info');
}
