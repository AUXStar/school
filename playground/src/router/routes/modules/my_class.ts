import type { RouteRecordRaw } from 'vue-router';

import { BasicLayout } from '#/layouts';
import { $t } from '#/locales';

const routes: RouteRecordRaw[] = [
  {
    component: BasicLayout,
    meta: {
      icon: 'mdi:account-box-multiple-outline',
      order: 100,
      title: $t('page.myClass.title'),
    },
    name: 'MyClass',
    path: '/my_class',
    children: [
      {
        meta: {
          icon: 'mdi:align-horizontal-left',
          title: $t('page.myClass.summary.title'),
        },
        name: 'Summary',
        path: '/my_class/summary',
        component: () => import('#/views/my_class/summary/index.vue'),
      },
      {
        meta: {
          icon: 'mdi:align-horizontal-left',
          title: $t('page.myClass.application.title'),
        },
        name: 'Application',
        path: '/my_class/application',
        children: [
          {
            meta: {
              icon: 'mdi:align-horizontal-left',
              title: $t('page.myClass.application.leave.title'),
            },
            name: 'Leave',
            path: '/my_class/application/leave',
            component: () => import('#/views/my_class/application/leave.vue'),
          },
        ],
      },
    ],
  },
];

export default routes;
