<template>
  <div class="left">
          <div class='box'>
            <p class='shangyinhao'>
              <img  src='../../img/shangyinhao.png'>
            </p>
            <p class='content'>
              愿你在我看不到的地方安然无恙<br />
              愿你的冬天永远不缺暖阳<br />
              愿你的明天不再经历雨打风霜<br />
              愿你的未来永远热泪盈眶<br />
            </p>
            <p class='cnt_footer'>
              by~邵帅《你是人间四月天》
            </p>
            <p class='xiayinhao'>
              <img  src='../../img/xiayinhao.png'>
            </p>
          </div>
          <div class='box'>
            <p class='shangyinhao'>
              <img  src='../../img/shangyinhao.png'>
            </p>
            <p class='content'>
               人一生，诗两行<br />
            </p>
            <p class='cnt_footer'>
              by~CSJerry
            </p>
            <p class='xiayinhao'>
              <img  src='../../img/xiayinhao.png'>
            </p>
          </div>
        </div>
</template>

<script>
export default {
name:'Left'
}
</script>

<style lang='less' scoped>
.left{
  padding: 30px;
  max-width: 385px;
  float: right;
  
  .box{
    background: rgb(255, 252, 247);
    box-shadow: 0 0 10px #ccc;
    padding: 20px;
    margin-bottom: 50px;
    border-radius: 8px;
  }
  img{
    width: 18px;
    height: 18px;
  }
  .shangyinhao{
    padding-left: 10px;
  }
  .xiayinhao{
    text-align: right;
    padding-right:10px;
  }
  .content{
    padding:20px;
    text-align: center;
  }
  .cnt_footer{
    text-align: right;
  }
}

</style>