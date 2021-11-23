<template>
  <div>
    <div>
      <div id="title">
      <a-popconfirm
        title="确定不保存就返回吗?"
        ok-text="Yes"
        cancel-text="No"
        @confirm="$router.go(-1);"
      >
        <a-button><a-icon type="left" />Go back </a-button>
      </a-popconfirm>
      <a-input placeholder="请输入标题" v-model='title' />
      <a-button @click='showExt'><a-icon type="check" /> 发布 </a-button>
      </div>
    <br />
    <mavon-editor
      id="edit"
      ref="edit"
      v-model="value"
      @save="save"
      @imgAdd="imgAdd"
      @imgDel="imgDel"
    />
    <!-- <a-button @click='uploadimg'>保存图片</a-button> -->
    </div>
    <div class="select">
      <a-drawer
      placement="right"
      :closable="false"
      :visible="select"
      @close="$data.select = false"
    >
      <get-ext @comfirm="save" />
    </a-drawer>
    </div>
  </div>
</template>

<script>
import getExt from '@/edit/getExt';
export default {
  name: "Edit",
  components:{
    getExt
  },
  data() {
    return {
      value: null,
      img_file: null,
      title: null,
      select: false
    };
  },
  methods: {
    // 展示选择标签页
    showExt(){
      this.select = true
    },
    // 保存文章
    async save(params) {
      console.log(this.title, params)
      if( this.title == null || this.title == ""){
        return this.$message.warning("标题不能为空哦")
      }
      if (this.img_file != null) {
        this.$message.info("正在上传图片");
        await this.uploadimg();
      }
      const { title, value: body } = this
      try {
        const res = await this.$api.Article.save({ 
          title,
          body,
          categories: params.categories,
          tags: params.tags
        })
        console.log("保存文章的结果", res)
        if(res.data.flag){
          this.$message.success("发布成功")
          this.$router.push('/')
        }else{
          this.$message.warning("发布失败")
        }
      } catch (error) {
        this.$message.warning('只有第一作者可以发布文章哦')
      }

    },
    imgAdd(pos, $file) {
      console.log("添加图片", pos, $file);
      // 缓存图片信息
      this.img_file[pos] = $file;
    },
    imgDel(pos) {
      delete this.img_file[pos[0]];
    },
    async uploadimg() {
      // 第一步.将图片上传到服务器.
      var formdata = new FormData();
      console.log(this.img_file[1]);
      for (let _img in this.img_file) {
        // console.log(_img);
        formdata.append(_img, this.img_file[_img]);
      }

      // console.log("图片数据", formdata)
      const result = await this.$api.Upload.img(formdata);
      // console.log("上传图片的结果", result)
      if (result.status === 201) {
        // 替换源文本的图片链接
        this.$message.success("图片上传成功");
        const $img = this.$refs.edit;

        // 数据清洗
        const imgs = Object.keys(result.data.files).map((key) => {
          // console.log(key)
          return [Number(key), result.data.files[key][0]];
        });
        // console.log(imgs)
        for (let img of imgs) {
          $img.$img2Url(img[0], img[1].path);
        }
      } else {
        this.$message.error("上传失败");
      }
    },

  },
};
</script>

<style lang='less' scoped>
#title {
  margin-top:10px;
  display: flex;
}
#edit {
  height: 800px;
  z-index: 0;
}
</style>