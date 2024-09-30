<script setup lang="ts">
import type { AboutProps, DescriptionItem } from './about';

import { h } from 'vue';

import { VbenLink, VbenRenderContent } from '@vben-core/shadcn-ui';

import { Page } from '../../components';

interface Props extends AboutProps {}

defineOptions({
  name: 'AboutUI',
});

withDefaults(defineProps<Props>(), {
  description:
    '作为一款引领未来教育潮流的综合性智慧平台，深刻洞察并从根本上重塑了学生在校生活的全貌。该平台巧妙融合先进的人工智能大模型，对学生的日常行为与学习轨迹进行深度剖析与智能化引导，开创性地将科技力量注入教育的每一个细微之处。\n我们创新性地引入嵌入智能技术的手表、校服及校徽，集成了GPS与室内蓝牙精确定位系统，构筑起无微不至的安全守护网，实现对学生安全的全天候、无缝隙监控。同时，通过与校园摄像头系统的无缝对接及高级人脸识别技术，我们构建了一个既安全又高效的数字化校园环境，确保每位学生的福祉得到最大化的保障。\n在学习领域，宁静云校园通过精密的数据追踪与分析，为每位学生绘制个性化成长蓝图，精准把握学习动态，助力教育者量身定制教学方案。平台集课程资源、智能统计分析、个性化学习建议于一体，不仅赋能教师精准施教，更为家长开启了一扇全面了解孩子学习进程的窗口。\n更进一步，宁静云校园通过实时校内通讯体系、课程智能提醒、以及高效作业发布与审批流程，极大地提升了教育管理的流畅度与透明度。班费管理模块的加入，则让财务管理变得公开透明，促进了家校间的信任与合作。\n总之，宁静云校园以其前瞻性的设计理念与尖端科技的应用，构建了一个智慧共生的教育生态，不仅重新定义了校园管理的高效与便捷，更为每一位学子的卓越成长铺设了坚实的道路，开启了智慧教育的新纪元。',
  name: '宁静云校园',
  title: '关于项目',
});

declare global {
  const __VBEN_ADMIN_METADATA__: {
    authorEmail: 'njzy4688@outlook.com';
    authorName: '王靖元';
    authorUrl: 'https://github.com/AUXStar/AUXStar';
    dependencies: Record<string, string>;
    description: string;
    devDependencies: Record<string, string>;
    homepage: string;
    license: string;
    repositoryUrl: string;
    version: string;
  };
}

const {
  dependencies = {},
  devDependencies = {},
  // vite inject-metadata 插件注入的全局变量
  // eslint-disable-next-line no-undef
} = __VBEN_ADMIN_METADATA__ || {};

const vbenDescriptionItems: DescriptionItem[] = [
  {
    content: h('div', [
      h(
        VbenLink,
        { class: 'mr-2', href: 'https://github.com/AUXStar/AUXStar' },
        { default: () => '王靖元' },
      ),
      h(
        VbenLink,
        { class: 'mr-2', href: 'mailto:njzy4688@outlook.com' },
        { default: () => 'njzy4688@outlook.com' },
      ),
    ]),
    title: '作者',
  },
  {
    content: h('div', [
      h(
        VbenLink,
        { class: 'mr-2', href: 'tel:111-1111-1111' },
        { default: () => '邵芳德' },
      ),
      h(
        VbenLink,
        { class: 'mr-2', href: 'tel:111-1111-1111' },
        { default: () => '邓艳梅' },
      ),
      h(
        VbenLink,
        { class: 'mr-2', href: 'tel:111-1111-1111' },
        { default: () => '王英琴' },
      ),
    ]),
    title: '指导老师',
  },
];

const dependenciesItems = Object.keys(dependencies).map((key) => ({
  content: dependencies[key],
  title: key,
}));

const devDependenciesItems = Object.keys(devDependencies).map((key) => ({
  content: devDependencies[key],
  title: key,
}));
</script>

<template>
  <Page :title="title">
    <template #description>
      <p class="text-foreground mt-3 text-sm leading-6">
        <VbenLink href="/">
          {{ name }}
        </VbenLink>
        {{ description }}
      </p>
    </template>
    <div class="card-box p-5">
      <div>
        <h5 class="text-foreground text-lg">基本信息</h5>
      </div>
      <div class="mt-4">
        <dl class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
          <template v-for="item in vbenDescriptionItems" :key="item.title">
            <div class="border-border border-t px-4 py-6 sm:col-span-1 sm:px-0">
              <dt class="text-foreground text-sm font-medium leading-6">
                {{ item.title }}
              </dt>
              <dd class="text-foreground mt-1 text-sm leading-6 sm:mt-2">
                <VbenRenderContent :content="item.content" />
              </dd>
            </div>
          </template>
        </dl>
      </div>
    </div>

    <div class="card-box mt-6 p-5">
      <div>
        <h5 class="text-foreground text-lg">生产环境依赖</h5>
      </div>
      <div class="mt-4">
        <dl class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
          <template v-for="item in dependenciesItems" :key="item.title">
            <div class="border-border border-t px-4 py-3 sm:col-span-1 sm:px-0">
              <dt class="text-foreground text-sm">
                {{ item.title }}
              </dt>
              <dd class="text-foreground/80 mt-1 text-sm sm:mt-2">
                <VbenRenderContent :content="item.content" />
              </dd>
            </div>
          </template>
        </dl>
      </div>
    </div>
    <div class="card-box mt-6 p-5">
      <div>
        <h5 class="text-foreground text-lg">开发环境依赖</h5>
      </div>
      <div class="mt-4">
        <dl class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
          <template v-for="item in devDependenciesItems" :key="item.title">
            <div class="border-border border-t px-4 py-3 sm:col-span-1 sm:px-0">
              <dt class="text-foreground text-sm">
                {{ item.title }}
              </dt>
              <dd class="text-foreground/80 mt-1 text-sm sm:mt-2">
                <VbenRenderContent :content="item.content" />
              </dd>
            </div>
          </template>
        </dl>
      </div>
    </div>
  </Page>
</template>
