<template>
  <div>
    <a-card title='分类管理'>
    <a-button id='addbtn' @click='$data.visible = true'>添加分类</a-button>
    <a-modal
      title="添加分类"
      :visible="visible"
      @ok="addCategory"
      @cancel="$data.visible = false"
    >
      <a-space>
        <a-space>
          <a-input  v-model='obj.title' placeholder='请输入分类标题'/>
          <a-input v-model='obj.description' placeholder='请输入分类描述'/>
        </a-space>
      </a-space>
    </a-modal>
    <a-table bordered :data-source="dataSource" :columns="columns" rowKey="title">
      <template slot="operation" slot-scope="text, record">
        <a-popconfirm
          v-if="dataSource.length"
          title="确认删除吗?"
          @confirm="() => onDelete(record)"
        >
          <a href="javascript:;">删除</a>
        </a-popconfirm>
        <a-divider type="vertical" />
      </template>
    </a-table>
    </a-card>
  </div>
</template>
<script>
import columns from './columns.js';

export default {
  data() {
    return {
      columns,
      dataSource: [], 
      api: this.$api.Categories,
      visible: false,
      obj: {
        title: null,
        description: null
      }
    };
  },
  mounted(){
    this.get()
  },
  methods: {
    get(){
      this.api.getCategories().then(r=>{
        this.dataSource = r.data.categories.categories
      })
    },
    addCategory(){
      this.api.addCategory({category:this.obj}).then(r=>{
        if(r.data.flag){
          this.$message.success('添加成功')
          this.get()
          this.visible = false
        }else{
          this.$message.error(r.data.msg)
        }
      })
    },
    onDelete(record) {
      console.log(record)
      this.api.del({id: record._id}).then(r=>{
        if(r.data.flag) {
          this.$message.success('删除成功')
          this.get()
        }else{
          this.$message.warning('发生错误')
        }
      })
    }
  },
};
</script>
<style scoped lang='less'>
#addbtn{
  margin-bottom: 20px;
}
.editable-cell {
  position: relative;
}

.editable-cell-input-wrapper,
.editable-cell-text-wrapper {
  padding-right: 24px;
}

.editable-cell-text-wrapper {
  padding: 5px 24px 5px 5px;
}

.editable-cell-icon,
.editable-cell-icon-check {
  position: absolute;
  right: 0;
  width: 20px;
  cursor: pointer;
}

.editable-cell-icon {
  line-height: 18px;
  display: none;
}

.editable-cell-icon-check {
  line-height: 28px;
}

.editable-cell:hover .editable-cell-icon {
  display: inline-block;
}

.editable-cell-icon:hover,
.editable-cell-icon-check:hover {
  color: #108ee9;
}

.editable-add-btn {
  margin-bottom: 8px;
}
</style>