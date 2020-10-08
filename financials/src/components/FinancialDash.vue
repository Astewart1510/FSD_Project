<template>
  <div class="main">
    <h1>AIFMRM - Equity Risk Service (ERS)</h1>
      <div class="row">
      <div class="col-md-3">
      </div>
      <div class="col-md-3">
      <b-form-select v-model="selectedIndex" :options="IndexOptions" size="sm" class="mt-3"></b-form-select>
      <div class="mt-3">Selected: <strong>{{ selectedIndex }}</strong></div>
      </div>
      <!-- Have to update page only after both options have been selected -->
      <div class="col-md-3">
      <b-form-select v-model="selectedJSE" :options="JSEoptions" size="sm" class="mt-3"></b-form-select>
      <div class="mt-3">Selected: <strong>{{ selectedJSE }}</strong></div>
      </div>
    </div>

    <!-- <div class="div" v-if="selectedIndex !== null & selectedJSE !== null">  -->
      <div>
        <b-table striped hover :items="items" :fields="fields"></b-table>
      </div>
    

      <div class="row">
        <div class="col-md-4">
        </div>
        <div class="col-md-4">
          <b-form-select v-model="selectedPlot" :options="PlotOptions" size="sm" class="mt-3"  v-on:change="getSelectedItem"></b-form-select>
          <div class="mt-3">Selected: <strong>{{ selectedPlot }}</strong></div>
        </div>
      </div>  

      <!-- <div class="div" v-if="selectedPlot !== null">  -->
      <div id='myDiv'></div>
      <!-- </div> -->

      <button onClick="window.location.reload();">Reset Page</button>
    <!-- </div>   -->

  </div>
</template>

<script>

import axios from 'axios'
import Plotly from 'plotly.js-dist';

var data = [
  {
    x: ['giraffes', 'orangutans', 'monkeys'],
    y: [20, 14, 23],
    type: 'bar'
  }
];

// Plotly.newPlot('myDiv', data);

export default {
  name: 'FinancialDash',
  props: {
    msg: String
  },

  methods: {

    // getTable() {
    //   axios.get('https://financialmodelingprep.com/api/v3/income-statement/AAPL?period=quarter&limit=400&apikey=ad8589337943450d30eab43989baa1e3')
    //   .then( res => {
    //     this.IStemp = res.data
    //     this.IStemp = this.IStemp.slice(0,5)
    //     for (this.xi of this.IStemp) {
    //       this.revenue.push(this.xi.revenue/1000000)
    //       this.COGS.push(this.xi.costOfRevenue/1000000)
    //       this.GrossProfit.push(this.xi.grossProfit/1000000)
    //       this.Opinc.push(this.xi.operatingIncome/1000000)
    //       this.Netinc.push(this.xi.netIncome/1000000)
    //       this.ISdate.push(this.xi.date)
    //     }
    //     console.log(this.revenue)
    //   })
    //   .catch(err => console.log(err))
    // },

    

    getSelectedItem: function(myarg) { // Just a regular js function that takes 1 arg
        if (myarg == 'Weight') {
          Plotly.newPlot('myDiv', data);
        } else if (myarg == 'Beta') {

        } else if (myarg == 'Sysvol') {

        } else if (myarg == 'Specvar') {

        } 
        console.log(myarg);
    },

  },

  

  data() {
      return {
        index: '',
        proxy: '',
        xi: '',
        trace1: {},
        revenue: [],
        COGS: [],
        GrossProfit: [],
        Opinc: [],
        Netinc: [],
        ISdate: [],
        IStemp: '',

        selectedIndex: null,
        IndexOptions: [
          { value: null, text: 'Please select the index' },
          { value: 'ALSI', text: 'All Share Index (ALSI)' },
          { value: 'FLED', text: 'Fledging Index (FLED)' },
          { value: 'LRGC', text: 'Large Cap Index (LRGC)' },
          { value: 'MIDC', text: 'Mid Cap Index (MIDC)' },
          { value: 'SMLC', text: 'Small Cap Index (SMLC)' },
          { value: 'TOPI', text: 'Top 40 Index (TOPI)' },
          { value: 'RESI', text: 'Resource 20 Index (RESI)' },
          { value: 'FINI', text: 'Financial 15 Index (FINI)' },
          { value: 'INDI', text: 'Industrial 25 Index (INDI)' },
          { value: 'PCAP', text: 'Capped Property Index (PCAP)' },
          { value: 'SAPY', text: 'SA Listed Property Index (SAPY)' },
          { value: 'ALTI', text: 'Africa Alternative Index (ALTI)' },
          // { value: { M: '3PO' }, text: 'This is an option with object value' },
          // { value: 'z', text: 'This one is disabled', disabled: true }
        ],
        selectedJSE: null,
        JSEoptions: [
          { value: null, text: 'Please select the market proxy' },
          { value: 'J203', text: 'All Share (J203)' },
          { value: 'J200', text: 'Top 40 (J200)' },
          { value: 'J250', text: 'Financials and Industrials (J250)' },
          { value: 'J257', text: 'Industrials (J257)' },
          { value: 'J258', text: 'Resources (J258)' },
          // { value: { C: '3PO' }, text: 'This is an option with object value' },
          // { value: 'z', text: 'This one is disabled', disabled: true }
        ],
        selectedPlot: null,
        PlotOptions: [
          { value: null, text: 'Please select the plot required' },
          { value: 'Weight', text: 'Weight Decomposition'},
          { value: 'Beta', text: 'Beta Decomposition' },
          { value: 'Sysvol', text: 'Systematic Volatility Decomposition' },
          { value: 'Specvar', text: 'Specific Variance Decomposition' },
          // { value: { C: '3PO' }, text: 'This is an option with object value' },
          // { value: 'z', text: 'This one is disabled', disabled: true }
        ],

        fields: ['quarter', 'industry', 'weight','beta','SysVol', 'SpecVar'],
        items: [
          { quarter: '2017-Q3', industry: 'Gas and Oil', weight: '0.4', beta : 0.8, SysVol: 0.7, SpecVar: 0.6 },
          { quarter: '2017-Q3', industry: 'Utilities', weight: '0.6', beta : 0.8, SysVol: 0.7, SpecVar: 0.6 },
        ], 
        
      }
    }

    
  
}


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  margin: 20px 0 10px;
  color: rgb(0, 0, 0)
}

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

.headingcustomtable{
  color:rgba(30, 113, 184, 1);
}
</style>
