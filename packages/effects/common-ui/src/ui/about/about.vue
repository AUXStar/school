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
      <div class="mt-6">
        <div class="card-box rounded-lg p-5 shadow-md">
          <h2 class="mb-4 text-3xl font-bold">项目简介</h2>
          <div class="space-y-4">
            <div class="rounded p-4 shadow-inner">
              <h3 class="text-xl font-semibold">未来教育愿景</h3>
              <p>
                宁静云校园，致力于成为教育4.0时代的先行者，通过深度融合AI技术与教育实践，为学生打造个性化、智能化的学习体验。我们的愿景是消除学习障碍，激发每个孩子的潜能，促进全球教育公平与质量的双重提升。
              </p>
            </div>
            <div class="rounded p-4 shadow-inner">
              <h3 class="text-xl font-semibold">核心功能亮点</h3>
              <ul class="list-inside list-disc">
                <li>
                  智能安全监护：集成智能穿戴设备，实现24小时安全定位与异常行为预警。
                </li>
                <li>
                  个性化学习路径：根据学生能力与兴趣定制学习计划，精准推送教育资源。
                </li>
                <li>
                  高效教学管理：一键发布作业与通知，智能评估学习成效，减轻教师负担。
                </li>
                <li>
                  家校互动平台：建立透明的家校沟通桥梁，增进双方理解与合作，共促学生成长。
                </li>
              </ul>
            </div>
            <div class="rounded p-4 shadow-inner">
              <h3 class="text-xl font-semibold">技术创新应用</h3>
              <p>
                利用大数据分析与机器学习算法，深入分析学生学习习惯与成效，不断优化推荐算法，使教育更加智能化。同时，结合物联网技术，创造沉浸式学习环境，让学生在互动与实践中深化知识掌握。
              </p>
            </div>
          </div>
        </div>
      </div>
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
