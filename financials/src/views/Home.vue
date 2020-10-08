<template>
  <div class="home">
    <img alt="Page header" src="../assets/uct.jpg">
    <FinancialDash/>
    <img alt="Page footer" src="../assets/test.png" height="300px" width="1000px">
  </div>
</template>


<script>
// @ is an alias to /src
import FinancialDash from '@/components/FinancialDash.vue'

export default {
  name: 'Home',
  components: {
    FinancialDash
  }
}
</script>
