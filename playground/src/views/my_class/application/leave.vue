<script lang="ts" setup>
import { Page } from '@vben/common-ui';

import { Button, Card, message } from 'ant-design-vue';

import { useVbenForm } from '#/adapter';
import { $t } from '#/locales';

const [Form, formApi] = useVbenForm({
  // 所有表单项共用，可单独在表单内覆盖
  commonConfig: {
    // 所有表单项
    componentProps: {
      class: 'w-full',
    },
  },
  // 使用 tailwindcss grid布局
  // 提交函数
  handleSubmit: onSubmit,
  // 垂直布局，label和input在不同行，值为vertical
  layout: 'horizontal',
  // 水平布局，label和input在同一行
  schema: [
    {
      // 组件需要在 #/adapter.ts内注册，并加上类型
      component: 'RangePicker',
      // 对应组件的参数
      componentProps: {
        placeholder: ['开始', '结束'],
      },
      // 字段名
      fieldName: 'dates',
      // 界面显示的label
      label: $t('page.myClass.application.leave.dates'),
      rules: 'required',
    },
    {
      component: 'TimePicker',
      fieldName: 'from',
      label: $t('page.myClass.application.leave.from'),
      rules: 'required',
    },
    {
      component: 'TimePicker',
      fieldName: 'to',
      label: $t('page.myClass.application.leave.to'),
      rules: 'required',
    },
    {
      component: 'Textarea',
      fieldName: 'reason',
      label: $t('page.myClass.application.leave.reason'),
      rules: 'required',
    },
    {
      component: 'Checkbox',
      fieldName: 'checkbox',
      label: '',
      renderComponentContent: () => {
        return {
          default: () => ['我已阅读并同意'],
        };
      },
      rules: 'required',
    },
  ],
  // 大屏一行显示3个，中屏一行显示2个，小屏一行显示1个
  wrapperClass: 'grid-cols-1 md:grid-cols-1 lg:grid-cols-2',
});

function onSubmit(values: Record<string, any>) {
  message.success({
    content: `form values: ${JSON.stringify(values)}`,
  });
}
</script>

<template>
  <Page :title="$t('page.myClass.application.leave.title')">
    <Card title="基础组件校验示例">
      <template #extra>
        <Button @click="() => formApi.validate()">校验表单</Button>
        <Button class="mx-2" @click="() => formApi.resetValidate()">
          清空校验信息
        </Button>
      </template>
      <Form />
    </Card>
  </Page>
</template>
