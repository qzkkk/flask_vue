<template>
  <div>
    <div class="selectTags">
      <a-space direction="vertical" align='center' >
        <a-card class="select" title="选择分类">
          <a-select
            mode="multiple"
            :default-value="[]"
            style="width: 100%"
            placeholder="请选择分类"
            @change="handleChange"
          >
            <a-select-option v-for="i in categories" :key="i">
              {{ i }}
            </a-select-option>
          </a-select>
        </a-card>
        <a-card class="select" title="选择标签">
          <template v-for="tag in tags">
            <a-tooltip v-if="tag.length > 20" :key="tag" :title="tag">
              <a-tag
                :key="tag"
                @close="() => handleClose(tag)"
                color="red"
                :closable="true"
              >
                {{ `${tag.slice(0, 20)}...` }}
              </a-tag>
            </a-tooltip>
            <a-tag
              color="cyan"
              v-else
              :key="tag"
              :closable="true"
              @close="() => handleClose(tag)"
            >
              {{ tag }}
            </a-tag>
          </template>
          <a-input
            v-if="inputVisible"
            ref="input"
            type="text"
            size="small"
            :style="{ width: '78px' }"
            :value="inputValue"
            @change="handleInputChange"
            @blur="handleInputConfirm"
            @keyup.enter="handleInputConfirm"
          />
          <a-tag
            v-else
            style="background: #fff; borderstyle: dashed"
            color="blue"
            @click="showInput"
          >
            <a-icon type="plus" /> New Tag
          </a-tag>
        </a-card>
        <a-popconfirm title="选择完标签了吗？" ok-text="Yes" cancel-text="No" @confirm='confirmSave'>
          <a-button type="primary" ghost >确认发布</a-button>
        </a-popconfirm>
      </a-space>
    </div>
  </div>
</template>

<script>
export default {
  name: "GetExt",
  data() {
    return {
      tags: [],
      categories:[],
      articleCategories:[],
      inputVisible: false,
      inputValue: "",
    };
  },
  async mounted(){
    this.getCategories()
    this.getTags()
  },
  methods: {
    addtag(name){
      this.$api.Tags.add({name}).then(r=>{
        const {flag, tags, msg} = r.data
        if(flag){
          this.tags = tags.tags
        }else{
          this.$message.error(msg)
        }
      }).then(()=>{
        this.inputVisible = false,
        this.inputValue = ""
      })
    },
    getCategories(){
    //   获取用户的分类
    this.$api.Categories.getCategories().then(r=>{
      // console.log(r)
      this.categories = r.data.categories.categories.map(i=>{
        // console.log('i', i)
        return i.title
      },()=>{
        this.$message.error("网络出错啦")
      })
    })
    },
    getTags(){
      this.$api.Tags.get().then(r=>{
        const {flag,tags, msg} = r.data
        console.log(tags)
        if( flag ){
          this.tags = tags[0].tags
          // console.log(this.tags)
        }else{
          this.$message.error( msg )
        }
      },()=>{
        this.$message.errror("网络出错啦")
      })
    },
    handleClose(removedTag) {
      const tags = this.tags.filter((tag) => tag !== removedTag);
      // console.log(tags);
      this.tags = tags;
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(function () {
        this.$refs.input.focus();
      });
    },

    handleInputChange(e) {
      this.inputValue = e.target.value;
    },

    handleInputConfirm() {
      const inputValue = this.inputValue;
      this.addtag(inputValue)
    },

    // 选择分类
    handleChange(value) {
      this.articleCategories = [...value]
    },
    // 确认发布
    confirmSave(){
        this.$emit("comfirm", { tags:this.tags, categories: this.articleCategories } )
    }
  },
};
</script>

<style lang='less' scoped>
.select {
  min-height: 150px;
  width:210px;
}
.send {
  display: flex;
}
</style>