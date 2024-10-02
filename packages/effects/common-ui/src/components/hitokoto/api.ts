import { ref } from 'vue';

import axios from 'axios';

export type HitokotoResponse = {
  commit_from: string;
  created_at: number;
  creator: string;
  creator_uid: number;
  from: string;
  from_who: string;
  hitokoto: string;
  id: number;
  length: number;
  reviewer: number;
  type: string;
  uuid: string;
};
let hitokotoCache: HitokotoResponse | null = null;

export const hitokoto_ref = ref<HitokotoResponse | null>(null);

export async function refresh_hitokoto(useCache = true): Promise<void> {
  hitokoto_ref.value = await getHitokoto(useCache);
}

export async function getHitokoto(useCache = true): Promise<HitokotoResponse> {
  if (useCache && hitokotoCache !== null) {
    return hitokotoCache;
  }
  try {
    const response = await axios.get('https://v1.hitokoto.cn/?c=d&c=i');
    const data = response.data as HitokotoResponse;
    hitokotoCache = data;

    return data;
  } catch {
    try {
      const response = await axios.get(
        'https://international.v1.hitokoto.cn/?c=d&c=i',
      );
      const data = response.data as HitokotoResponse;
      hitokotoCache = data;
      return data;
    } catch (error) {
      console.error('获取一言时出错:', error);
      throw error;
    }
  }
}
