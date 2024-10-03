import type { LoginParams, RegisterParams } from '@vben/common-ui';
import type { UserInfo } from '@vben/types';

import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { DEFAULT_HOME_PATH, LOGIN_PATH } from '@vben/constants';
import { resetAllStores, useAccessStore, useUserStore } from '@vben/stores';

import { notification } from 'ant-design-vue';
import { defineStore } from 'pinia';

import { getUserSelfInfoApi, loginApi, logoutApi, registerApi } from '#/api';
import { $t } from '#/locales';

export const useAuthStore = defineStore('auth', () => {
  const accessStore = useAccessStore();
  const userStore = useUserStore();
  const router = useRouter();

  const loginLoading = ref(false);

  /**
   * 异步处理登录操作
   * Asynchronously handle the login process
   * @param params 登录表单数据
   * @param onSuccess 成功之后的回调函数
   */
  async function authLogin(
    params: LoginParams,
    onSuccess?: () => Promise<void> | void,
  ) {
    try {
      loginLoading.value = true;
      const { id } = await loginApi(params);
      if (id !== -1) {
        accessStore.setAccessToken(id.toString());
        // 获取用户信息并存储到 accessStore 中
        const userInfo = await fetchUserInfo();

        userStore.setUserInfo(userInfo);

        if (accessStore.loginExpired) {
          accessStore.setLoginExpired(false);
        } else {
          onSuccess
            ? await onSuccess?.()
            : await router.push(DEFAULT_HOME_PATH);
        }

        if (userInfo?.realname) {
          notification.success({
            description: `${$t('authentication.loginSuccessDesc')}:${userInfo?.realname}`,
            duration: 3,
            message: $t('authentication.loginSuccess'),
          });
        }
      } else {
        throw new Error('Login failed');
      }
    } catch (error) {
      notification.error({
        message: $t('authentication.loginError'),
        duration: 3,
      });
      throw error;
    } finally {
      loginLoading.value = false;
    }

    return {
      userInfo,
    };
  }

  async function authRegister(
    params: RegisterParams,
    onSuccess?: () => Promise<void> | void,
  ) {
    try {
      loginLoading.value = true;
      const { id } = await registerApi(params);
      if (id !== -1) {
        accessStore.setAccessToken(id.toString());
        // 获取用户信息并存储到 accessStore 中
        const userInfo = await fetchUserInfo();

        userStore.setUserInfo(userInfo);

        if (accessStore.loginExpired) {
          accessStore.setLoginExpired(false);
        } else {
          onSuccess
            ? await onSuccess?.()
            : await router.push(DEFAULT_HOME_PATH);
        }

        if (userInfo?.realname) {
          notification.success({
            description: `${$t('authentication.registerSuccessDesc')}:${userInfo?.realname}`,
            duration: 3,
            message: $t('authentication.registerSuccess'),
          });
        }
      } else {
        throw new Error('Register failed');
      }
    } catch (error) {
      notification.error({
        message: $t('authentication.registerError'),
        duration: 3,
      });
      throw error;
    } finally {
      loginLoading.value = false;
    }

    return {
      userInfo,
    };
  }

  async function logout(redirect: boolean = true) {
    await logoutApi();

    resetAllStores();
    accessStore.setLoginExpired(false);

    // 回登陆页带上当前路由地址
    await router.replace({
      path: LOGIN_PATH,
      query: redirect
        ? {
            redirect: encodeURIComponent(router.currentRoute.value.fullPath),
          }
        : {},
    });
  }

  async function fetchUserInfo() {
    let userInfo: null | UserInfo = null;
    userInfo = await getUserSelfInfoApi();
    userStore.setUserInfo(userInfo);
    return userInfo;
  }

  function $reset() {
    loginLoading.value = false;
  }

  return {
    $reset,
    authLogin,
    authRegister,
    fetchUserInfo,
    loginLoading,
    logout,
  };
});
