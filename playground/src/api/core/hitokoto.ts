import { useUserStore } from '@vben/stores';

import axios from 'axios';

export async function hitokotoApi() {
  const userStore = useUserStore();
  const data = await getHitokoto();
  userStore.setHitokoto(
    `${data.hitokoto} \n --${data.from_who} · ${data.from}`,
  );
}

export async function getHitokoto() {
  let _: any;
  await axios
    .get('https://v1.hitokoto.cn/?c=d&c=i')
    .then(({ data }) => {
      _ = data;
    })
    .catch(({ reason }) => {
      reason;
    });
  return _;
}
