<template>
  <div id='page'>
    <div class="content">
            <a-row>
        <a-col :lg='7' :md='0' :xs='0'>
          <Left />
        </a-col>
        <a-col :lg='10' :md='24' :xs='24'>
          <Show />
        </a-col>
        <a-col :lg='7' :md='0' :xs='0'>
          <Right />
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script>
import Show from '@/Index/Show'
import Left from '@/Index/Left'
import Right from '@/Index/Right'
export default {
  name:'Index',
  components:{
    Show,
    Left,
    Right
  },
  data(){
    return {

    }
  }
};
</script>

<style lang='less' scoped>
#page{
  padding: 30px;
  height: 100%;
}

@media screen and (max-width:1200px) {
  #page{
    padding: 30px 0;
  }
}

</style>