<template>
  <div class="hello">
    <div class="container">
      <form class="navbar-form m-2">
        <div class="input-group no border">
          <input type="text" value="" class="form-control" placeholder="Search..." v-model="stock">
            <button @click="update(stock)" class="btn btn-white btn-round btn-just-icon">
              <i class="material-icons ml-3">search</i>
            </button>
        </div>
      </form>
    </div>  
    
  </div>
</template>

<script>
export default {
  name: 'StockInfo',
  props: {
    msg: String
  },
  data() {
    return {
      stock: ""
    }
  },

  methods: {
    update(stock) {
      console.log(stock)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
