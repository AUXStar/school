<script lang="ts" setup>
import type { LoginCodeParams, VbenFormSchema } from '@vben/common-ui';

import { computed, ref } from 'vue';

import { AuthenticationCodeLogin, z } from '@vben/common-ui';
import { $t } from '@vben/locales';
import { authStore } from '@vben/auth-store';
import { notification } from '@vben/notification';

defineOptions({ name: 'CodeLogin' });

const loading = ref(false);

const formSchema = computed((): VbenFormSchema[] => {
  return [
    {
      component: 'VbenInput',
      componentProps: {
        placeholder: $t('authentication.mobile'),
      },
      fieldName: 'phoneNumber',
      label: $t('authentication.mobile'),
      rules: z
        .string()
        .min(1, { message: $t('authentication.mobileTip') })
        .refine((v) => /^\d{11}$/.test(v), {
          message: $t('authentication.mobileErrortip'),
        }),
    },
    {
      component: 'VbenPinInput',
      componentProps: {
        createText: (countdown: number) => {
          const text =
            countdown > 0
              ? $t('authentication.sendText', [countdown])
              : $t('authentication.sendCode');
          return text;
        },
        placeholder: $t('authentication.code'),
      },
      fieldName: 'code',
      label: $t('authentication.code'),
      rules: z.string().min(1, { message: $t('authentication.codeTip') }),
    },
  ];
});
/**
 * 异步处理登录操作
 * Asynchronously handle the login process
 * @param values 登录表单数据
 */
async function handleLogin(params: LoginCodeParams) {
    try {
        await authStore.authLogin(params);
    } catch (error) {
        notification.error({
            message: $t('authentication.loginError'),
            duration: 3,
        });
    }
}
</script>

<template>
  <AuthenticationCodeLogin
    :form-schema="formSchema"
    :loading="loading"
    @submit="handleLogin"
  />
</template>
