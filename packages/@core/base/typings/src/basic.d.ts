interface BasicOption {
  label: string;
  value: string;
}

type SelectOption = BasicOption;

type TabOption = BasicOption;

interface BasicUserInfo {
  avatar: string;
  is_male: boolean;
  permission_groups: string[];
  realname: string;
  username: string;
}

export type { BasicOption, BasicUserInfo, SelectOption, TabOption };
