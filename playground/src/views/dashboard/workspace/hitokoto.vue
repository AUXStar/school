<script lang="ts" setup>
import { getHitokoto } from '#/api/core/hitokoto';

const h = await getHitokoto();
</script>

<template>
  <h1>{{ h.from }}</h1>
</template>
