<template>
  <div v-if="(!menu.meta || !menu.meta.hidden) && showMenu()" class="sidebar-item">
    <el-sub-menu
      v-if="menu?.children && menu?.children.length > 0"
      :index="menu.path"
      popper-class="sidebar-container-popper"
    >
      <template #title>
        <!-- <el-icon>
          <AppIcon v-if="menu.meta && menu.meta.icon" :iconName="menuIcon" class="sidebar-icon" />
        </el-icon> -->
        <img v-if="menu.meta && menu.meta.icon" class="sidebar-img"  :src="returnImgSrc(menuIcon)" alt="">
        <span>{{ $t(menu.meta?.title as string) }}</span>
      </template>
      <sidebar-item
        v-hasPermission="child.meta?.permission"
        v-for="(child, index) in menu?.children"
        :key="index"
        :menu="child"
        :activeMenu="activeMenu"
      >
      </sidebar-item>
    </el-sub-menu>
    <el-menu-item
      v-else
      ref="subMenu"
      :index="menu.path"
      popper-class="sidebar-popper"
      @click="clickHandle(menu)"
    >
      <template #title>
        <!-- <AppIcon v-if="menu.meta && menu.meta.icon" :iconName="menuIcon" class="sidebar-icon" /> -->
         <img v-if="menu.meta && menu.meta.icon" class="sidebar-img"  :src="returnImgSrc(menuIcon)" alt="">
        <span v-if="menu.meta && menu.meta.title">{{ $t(menu.meta?.title as string) }}</span>
      </template>
    </el-menu-item>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter, useRoute, type RouteRecordRaw } from 'vue-router'
import { isWorkFlow } from '@/utils/application'
import userIcon from '@/assets/icon/user.png'
import userActiveIcon from '@/assets/icon/user-active.png'
import teamIcon from '@/assets/icon/team.png'
import teamActiveIcon from '@/assets/icon/team-active.png'
import templateIcon from '@/assets/icon/template.png'
import templateActiveIcon from '@/assets/icon/template-active.png'
import systemIcon from '@/assets/icon/settings.png'
import systemActiveIcon from '@/assets/icon/settings-active.png'
const props = defineProps<{
  menu: RouteRecordRaw
  activeMenu: any
}>()

const router = useRouter()
const route = useRoute()
const {
  params: { id, type }
} = route as any

function showMenu() {
  if (isWorkFlow(type)) {
    return props.menu.name !== 'AppHitTest'
  } else {
    return true
  }
}

function clickHandle(item?: any) {
  if (isWorkFlow(type) && item?.name === 'AppSetting') {
    router.push({ path: `/application/${id}/workflow` })
  }
}
const menuIcon = computed(() => {
  if (props.activeMenu === props.menu.path) {
    return props.menu.meta?.iconActive || props.menu?.meta?.icon
  } else {
    return props.menu?.meta?.icon
  }
})

const returnImgSrc = (icon: any) => {
  switch (icon) {
    case 'User':
      return userIcon
    case 'UserFilled':
      return userActiveIcon
    case 'app-team':
      return teamIcon
    case 'app-team-active':
      return teamActiveIcon
    case 'app-template':
      return templateIcon
    case 'app-template-active':
      return templateActiveIcon
      case 'app-setting':
      return systemIcon
    case 'app-setting-active':
      return systemActiveIcon
  }
}
</script>

<style scoped lang="scss">
.sidebar-item {
  .sidebar-icon {
    font-size: 20px;
    margin-top: -2px;
  }
  .sidebar-img{
    width: 22px;
    height: 22px;
    margin-right: 5px;
  }
  .el-menu-item {
    padding: 13px 12px 13px 16px !important;
    font-weight: 500;
    border-radius: 4px;
    &:hover {
      background: none;
      color: var(--el-color-primary);
    }
  }
  :deep(.el-sub-menu__title) {
    padding: 13px 12px 13px 16px !important;
    &:hover {
      background: none;
      color: var(--el-color-primary);
    }
  }
  .el-sub-menu {
    .el-menu-item {
      padding-left: 43px !important;
    }
  }
  .el-menu-item.is-active {
    color: var(--el-color-primary);
    background: var(--el-color-primary-light-9);
  }
}
</style>
