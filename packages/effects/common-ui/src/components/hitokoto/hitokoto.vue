<script lang="ts" setup>
import { onMounted } from 'vue';

import { Card, CardContent, CardHeader, CardTitle } from '@vben-core/shadcn-ui';

import { hitokoto_ref, refresh_hitokoto } from './api';

interface Props {
  title: string;
}

defineOptions({
  name: 'Hitokoto',
});

withDefaults(defineProps<Props>(), {});

onMounted(refresh_hitokoto);
</script>

<template>
  <Card>
    <CardHeader class="py-4">
      <CardTitle class="relative text-lg">
        {{ title }}
        <button
          class="absolute right-4 top-1/2 -translate-y-1/2 transform text-gray-500 hover:text-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-offset-2 dark:focus:ring-gray-600"
          style="background-color: transparent; border: none"
          @click="
            () => {
              refresh_hitokoto(false);
            }
          "
        >
          刷新
        </button>
      </CardTitle>
    </CardHeader>
    <CardContent class="flex flex-wrap p-5 pt-0">
      <div class="mx-auto w-full max-w-screen-md px-0">
        <h1 class="relative mb-4 text-3xl font-bold">
          <div class="flex flex-col items-center">
            <span class="ml-[-5%] self-start text-gray-500 dark:text-gray-400">
              『
            </span>
            <p
              class="m-0 mt-2 px-6 text-center text-gray-900 before:absolute before:left-1/2 before:top-0 before:-translate-x-1/2 dark:text-white"
            >
              {{ hitokoto_ref?.hitokoto || '行至水穷处，坐看云起时。' }}
            </p>
            <span class="mr-[-5%] self-end text-gray-500 dark:text-gray-400"> 』 </span>
          </div>
          <div
            class="mt-1 block text-right text-sm text-gray-500 dark:text-gray-400"
          >
            -&nbsp;
            <span
              v-if="
                (hitokoto_ref?.from_who && hitokoto_ref?.from) ||
                !hitokoto_ref?.from
              "
            >
              {{ hitokoto_ref?.from_who || '王维' }}&nbsp;·&nbsp;
            </span>
            《{{ hitokoto_ref?.from || '终南别业' }}》
          </div>
        </h1>
      </div>
    </CardContent>
  </Card>
</template>
