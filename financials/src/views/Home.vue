<template>
  <div class="home">
    <img alt="Page header" src="../assets/uct.jpg">
    <FinancialDash/>

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
