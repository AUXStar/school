import type { RouteRecordRaw } from 'vue-router';

import { BasicLayout } from '#/layouts';
import { $t } from '#/locales';

const routes: RouteRecordRaw[] = [
  {
    component: BasicLayout,
    meta: {
      icon: 'mdi:account-box-multiple-outline',
      keepAlive: true,
      order: 100,
      title: $t('page.myClass.title'),
    },
    name: 'MyClass',
    path: '/my_class',
    children: [
      // dsf
      {
        meta: {
          icon: 'mdi:align-horizontal-left',
          title: $t('page.myClass.summary.title'),
        },
        name: 'Summary',
        path: '/my_class/summary',
        component: () => import('#/views/my_class/summary.vue'),
      },
    ],
  },
];

export default routes;
