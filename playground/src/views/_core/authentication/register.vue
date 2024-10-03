<script lang="ts" setup>
import type { RegisterParams, VbenFormSchema } from '@vben/common-ui';

import { computed, h, ref } from 'vue';

import { AuthenticationRegister, z } from '@vben/common-ui';
import { $t } from '@vben/locales';

import { useAuthStore } from '#/store';

defineOptions({ name: 'Register' });

const authStore = useAuthStore();

const loading = ref(false);

const formSchema = computed((): VbenFormSchema[] => {
  return [
    {
      component: 'VbenInput',
      componentProps: {
        placeholder: $t('authentication.usernameTip'),
      },
      fieldName: 'username',
      label: $t('authentication.username'),
      rules: z.string().min(4, { message: $t('authentication.usernameErrorTip') }),
    },
    {
      component: 'VbenInput',
      componentProps: {
        placeholder: $t('authentication.realnameTip'),
      },
      fieldName: 'realname',
      label: $t('authentication.realname'),
      rules: z
        .string()
        .min(1, { message: $t('authentication.realnameErrorTip') })
        .refine((value) => /^[\u4e00-\u9fa5]+$/.test(value), {
          message: $t('authentication.realnameChineseErrorTip'),
        }),
    },
    {
      component: 'VbenInput',
      componentProps: {
        oninput: String.raw`this.value = this.value.replace(/[^0-9X]/g, '').replace(/^(.{18}).*$/, '$1')`,
        placeholder: $t('authentication.id_cardTip'),
      },
      fieldName: 'id_card',
      label: $t('authentication.id_card'),
      rules: z
        .string()
        .min(18, { message: $t('authentication.id_cardErrorTip') })
        .max(18, { message: $t('authentication.id_cardErrorTip') }),
    },
    {
      component: 'VbenInput',
      componentProps: {
        oninput: String.raw`this.value = this.value.replace(/\D/g, '')`,
        placeholder: $t('authentication.phoneTip'),
      },
      fieldName: 'phone',
      label: $t('authentication.phone'),
      rules: z.string().min(11, { message: $t('authentication.phoneErrorTip') }),
    },
    {
      component: 'VbenSelect',
      componentProps: {
        options: [
          {
            label: $t('authentication.genderMale'),
            value: 'male',
          },
          {
            label: $t('authentication.genderFemale'),
            value: 'female',
          },
        ],
        placeholder: $t('authentication.genderTip'),
      },
      fieldName: 'is_male',
      rules: z
        .enum(['male', 'female'])
        .optional()
        .refine((value) => value !== undefined, {
          message: $t('authentication.genderErrorTip'),
        }),
    },
    {
      component: 'VbenInputPassword',
      componentProps: {
        passwordStrength: true,
        placeholder: $t('authentication.password'),
      },
      fieldName: 'password',
      label: $t('authentication.password'),
      renderComponentContent() {
        return {
          strengthText: () => $t('authentication.passwordStrength'),
        };
      },
      rules: z.string().min(8, { message: $t('authentication.passwordErrorTip') }),
    },
    {
      component: 'VbenInputPassword',
      componentProps: {
        placeholder: $t('authentication.confirmPassword'),
      },
      dependencies: {
        rules(values) {
          const { password } = values;
          return z
            .string()
            .min(1, { message: $t('authentication.passwordTip') })
            .refine((value) => value === password, {
              message: $t('authentication.confirmPasswordErrorTip'),
            });
        },
        triggerFields: ['password'],
      },
      fieldName: 'confirmPassword',
      label: $t('authentication.confirmPassword'),
      rules: z.string().min(1, { message: $t('authentication.passwordTip') }),
    },
    {
      component: 'VbenCheckbox',
      fieldName: 'agreePolicy',
      renderComponentContent: () => ({
        default: () =>
          h('span', [
            $t('authentication.agree'),
            h(
              'a',
              {
                class:
                  'cursor-pointer text-primary ml-1 hover:text-primary-hover',
                href: '',
              },
              [
                $t('authentication.privacyPolicy'),
                '&',
                $t('authentication.terms'),
              ],
            ),
          ]),
      }),
      rules: z.boolean().refine((value) => !!value, {
        message: $t('authentication.agreePolicyErrorTip'),
      }),
    },
  ];
});

function handleSubmit(value: RegisterParams) {
  value.is_male = value.is_male === 'male';
  authStore.authRegister(value).catch(() => {
    notification.error({
      message: $t('authentication.registerError'),
      duration: 3,
    });
  });
}
</script>

<template>
  <AuthenticationRegister
    :form-schema="formSchema"
    :loading="loading"
    @submit="handleSubmit"
  />
</template>
