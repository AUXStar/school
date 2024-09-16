interface BasicOption {
  label: string;
  value: string;
}

type SelectOption = BasicOption;

type TabOption = BasicOption;

interface BasicUserInfo {
  avatar: string;
  nickname: string;
  permission_groups: string[];
  realname: string;
  username: string;
}

export type { BasicOption, BasicUserInfo, SelectOption, TabOption };
