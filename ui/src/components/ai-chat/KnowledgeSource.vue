<template>
  <div class="chat-knowledge-source">
    <!-- {{ data}} -->
    <div class="flex align-center mt-16" v-if="!isWorkFlow(props.type)">
      <span class="mr-4 color-secondary">{{ $t('chat.KnowledgeSource.title') }}</span>
      <el-divider direction="vertical" />
      <el-button type="primary" class="mr-8" link @click="openParagraph(data)">
        <AppIcon iconName="app-reference-outlined" class="mr-4"></AppIcon>
        {{ $t('chat.KnowledgeSource.referenceParagraph') }}
        {{ data.paragraph_list?.length || 0 }}
      </el-button>
    </div>
    <div class="mt-8" v-if="!isWorkFlow(props.type)">
      <el-row :gutter="8" v-if="uniqueParagraphList?.length">
        <template v-for="(item, index) in uniqueParagraphList" :key="index">
          <el-col :span="12" class="mb-8">
            <el-card shadow="never" class="file-List-card" data-width="40">
              <div class="flex-between">
                <div class="flex">
                  <img :src="getImgUrl(item && item?.document_name)" alt="" width="20" />
                  <div class="ml-4 ellipsis-1" :title="item?.document_name" v-if="!item.source_url">
                    <p>{{ item && item?.document_name }}</p>
                  </div>
                  <div class="ml-8" v-else>
                    <a :href="getNormalizedUrl(item?.source_url)" target="_blank" class="ellipsis"
                      :title="item?.document_name?.trim()">
                      <span :title="item?.document_name?.trim()">{{ item?.document_name }}</span>
                    </a>
                  </div>
                </div>
              </div>
            </el-card>
          </el-col>
        </template>
      </el-row>
    </div>

    <div class="execution-details border-t color-secondary flex-between mt-12"
      style="padding-top: 12px; padding-bottom: 8px">
      <div>
        <span class="mr-8">
          {{ $t('chat.KnowledgeSource.consume') }}: {{ data?.message_tokens + data?.answer_tokens }}
        </span>
        <span>
          {{ $t('chat.KnowledgeSource.consumeTime') }}: {{ data?.run_time?.toFixed(2) }} s</span>
      </div>
      <el-button v-if="isWorkFlow(props.type)" type="primary" link @click="openExecutionDetail(data.execution_details)"
        style="padding: 0;">
        <el-icon class="mr-4">
          <Document />
        </el-icon>
        {{ $t('chat.executionDetails.title') }}</el-button>
    </div>
    <div class="img-box">
      <div class="text-tip">引用</div>
      <template v-for="imgSrc in imgList" :key="imgSrc">
        <img :src="imgSrc" alt="" class="zoomable-image">
      </template>
    </div>
    <!-- 知识库引用 dialog -->
    <ParagraphSourceDialog ref="ParagraphSourceDialogRef" />
    <!-- 执行详情 dialog -->
    <ExecutionDetailDialog ref="ExecutionDetailDialogRef" />
  </div>
</template>
<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import ParagraphSourceDialog from './ParagraphSourceDialog.vue'
import ExecutionDetailDialog from './ExecutionDetailDialog.vue'
import { isWorkFlow } from '@/utils/application'
import { getImgUrl, getNormalizedUrl } from '@/utils/utils'
const props = defineProps({
  data: {
    type: Object,
    default: () => { }
  },
  type: {
    type: String,
    default: ''
  }
})

const ParagraphSourceDialogRef = ref()
const ExecutionDetailDialogRef = ref()
function openParagraph(row: any, id?: string) {
  ParagraphSourceDialogRef.value.open(row, id)
}
function openExecutionDetail(row: any) {
  ExecutionDetailDialogRef.value.open(row)
}
const uniqueParagraphList = computed(() => {
  const seen = new Set()
  return (
    props.data.paragraph_list?.filter((paragraph: any) => {
      const key = paragraph.document_name.trim()
      if (seen.has(key)) {
        return false
      }
      seen.add(key)
      // 判断如果 meta 属性不是 {} 需要json解析 转对象
      if (paragraph.meta && typeof paragraph.meta === 'string') {
        paragraph.meta = JSON.parse(paragraph.meta)
        paragraph.source_url = paragraph.meta.source_url
      }
      return true
    }) || []
  )
})

const imgList = computed(() => {
  let tempArray: string[] = []
  const origin = window.location.origin
  const execution_details = props.data.execution_details || []
  execution_details.forEach((item: any) => {
    let paragraph_list = item.paragraph_list
    if (paragraph_list) {
      paragraph_list.forEach((dataItem: any) => {
        const matches = dataItem.content.match(/!\[\]\(([^)]+)\)/g)
        if (matches) {
          matches.forEach((match: string) => {
            const content = match.replace(/!\[\]\(|\)/g, '')
            tempArray.push(origin + content)
          })
        }
      })
    }
  })
  return tempArray
})
import mediumZoom from 'medium-zoom';
onMounted(() => {
  mediumZoom('.zoomable-image', {
    margin: 20, // 可选，设置放大镜周围的边距
    background: '#00000080', // 可选，设置背景颜色和透明度
    scrollOffset: 60 // 可选，设置滚动偏移量以适应顶部导航栏等
  });
})
</script>
<style lang="scss" scoped>
@media only screen and (max-width: 420px) {
  .chat-knowledge-source {
    .execution-details {
      display: block;
    }
  }
}

.img-box {
  .zoomable-image {
    cursor: zoom-in;
    /* 鼠标悬停时显示放大镜图标 */
  }
  .text-tip {
    color: #646A73;
    border-bottom: 1px solid #dee0e3;
    margin-bottom: 5px;
  }
  img {
    width: 100%;
  }
}
</style>
