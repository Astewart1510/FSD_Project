<template>
  <div class="main">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">Headline</h1>

    </div>
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

    myProvider () {
        // Here we don't set isBusy prop, so busy state will be
        // handled by table itself
        // this.isBusy = true
        var JSEwebsite = ''

        if (this.selectedJSE == "J200") {
          JSEwebsite = 'http://financials.azurewebsites.net/api/J200/FetchAll'
        } else if (this.selectedJSE == "J203") {
          JSEwebsite ='http://financials.azurewebsites.net/api/J203/FetchAll'
        } else if (this.selectedJSE == "J250") {
          JSEwebsite = 'http://financials.azurewebsites.net/api/J250/FetchAll'
        } else if (this.selectedJSE == "J257") {
          JSEwebsite = 'http://financials.azurewebsites.net/api/J257/FetchAll'
        } else {
          JSEwebsite = 'http://financials.azurewebsites.net/api/J258/FetchAll'
        }

        let promise = axios.get(JSEwebsite)

        return promise.then((res) => {
          // console.log(res.data)
          const items = res.data
          // Here we could override the busy state, setting isBusy to false
          // this.isBusy = false

          this.IStemp1 = res.data
          console.log(res.data)

          this.Index_Code= []
          this.Date= []
          this.Industry = []
          this.Weight=[]
          this.pfBeta = []
          this.pfSysVol = []
          this.pfSpecVar = []

          for (this.yi of this.IStemp1) {

            this.Index_Code.push(this.yi.Index_Code)
            this.Date.push(this.yi.Date)
            this.Industry.push(this.yi.Industry)
            this.Weight.push(this.yi.Weight)
            this.pfBeta.push(this.yi.pfBeta)
            this.pfSysVol.push(this.yi.pfSysVol)
            this.pfSpecVar.push(this.yi.pfSpecVar)
          }

          if (this.selectedJSE !== this.previousSelection) {
            this.$refs.table.refresh()
            this.selectedPlot= null
          }
          this.previousSelection = this.selectedJSE
          console.log(this.pfBeta[0])
          return(items)
        }).catch(error => {
          // Here we could override the busy state, setting isBusy to false
          // this.isBusy = false
          // Returning an empty array, allows table to correctly handle
          // internal busy state in case of error
          return []
        })
      },

    getSelectedItem() { // Just a regular js function that takes 1 arg

      //   axios.get('http://financials.azurewebsites.net/api/ExclSpecVar/FetchAll')
      //   .then( res => {
      //   this.IStemp1 = res.data
      //   for (this.yi of this.IStemp1) {
      //     this.Index_Code.push(this.yi.Index_Code)
      //     this.Date.push(this.yi.Date)
      //     this.Industry.push(this.yi.Industry)
      //     this.Weight.push(this.yi.Weight)
      //     this.pfBeta.push(this.yi.pfBeta)
      //     this.pfSysVol.push(this.yi.pfSysVol)
      //   }

      // })
      // .catch(err => console.log(err))

        //console.log(this.Weight[0])

        if (this.selectedPlot == null) {

        } else {

        var x = 0

        if (this.selectedIndex == "ALSI") {
          x = 0
        } else if (this.selectedIndex == "ALTI") {
          x = 120
        } else if (this.selectedIndex == "FINI") {
          x = 240
        } else if (this.selectedIndex == "FLED") {
          x = 360
        } else if (this.selectedIndex == "INDI") {
          x = 480
        } else if (this.selectedIndex == "LRGC") {
          x = 600
        } else if (this.selectedIndex == "MIDC") {
          x = 720
        } else if (this.selectedIndex == "PCAP") {
          x = 840
        } else if (this.selectedIndex == "RESI") {
          x = 960
        } else if (this.selectedIndex == "SAPY") {
          x = 1080
        } else if (this.selectedIndex == "SMLC") {
          x = 1200
        } else if (this.selectedIndex == "TOPI") {
          x = 1320
        }

        var trace1 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[0+x], this.Weight[10+x], this.Weight[20+x],this.Weight[30+x], this.Weight[40+x], this.Weight[50+x],this.Weight[60+x], this.Weight[70+x], this.Weight[80+x],this.Weight[90+x], this.Weight[100+x], this.Weight[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[1+x], this.Weight[11+x], this.Weight[21+x],this.Weight[31+x], this.Weight[41+x], this.Weight[51+x],this.Weight[61+x], this.Weight[71+x], this.Weight[81+x],this.Weight[91+x], this.Weight[101+x], this.Weight[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[2+x], this.Weight[12+x], this.Weight[22+x],this.Weight[32+x], this.Weight[42+x], this.Weight[52+x],this.Weight[62+x], this.Weight[72+x], this.Weight[82+x],this.Weight[92+x], this.Weight[102+x], this.Weight[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[3+x], this.Weight[13+x], this.Weight[23+x],this.Weight[33+x], this.Weight[43+x], this.Weight[53+x],this.Weight[63+x], this.Weight[73+x], this.Weight[83+x],this.Weight[93+x], this.Weight[103+x], this.Weight[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[4+x], this.Weight[14+x], this.Weight[24+x],this.Weight[34+x], this.Weight[44+x], this.Weight[54+x],this.Weight[64+x], this.Weight[74+x], this.Weight[84+x],this.Weight[94+x], this.Weight[104+x], this.Weight[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[5+x], this.Weight[15+x], this.Weight[25+x],this.Weight[35+x], this.Weight[45+x], this.Weight[55+x],this.Weight[65+x], this.Weight[75+x], this.Weight[85+x],this.Weight[95+x], this.Weight[105+x], this.Weight[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[6+x], this.Weight[16+x], this.Weight[26+x],this.Weight[36+x], this.Weight[46+x], this.Weight[56+x],this.Weight[66+x], this.Weight[76+x], this.Weight[86+x],this.Weight[96+x], this.Weight[106+x], this.Weight[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[7+x], this.Weight[17+x], this.Weight[27+x],this.Weight[37+x], this.Weight[47+x], this.Weight[57+x],this.Weight[67+x], this.Weight[77+x], this.Weight[87+x],this.Weight[97+x], this.Weight[107+x], this.Weight[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[8+x], this.Weight[18+x], this.Weight[28+x],this.Weight[38+x], this.Weight[48+x], this.Weight[58+x],this.Weight[68+x], this.Weight[78+x], this.Weight[88+x],this.Weight[98+x], this.Weight[108+x], this.Weight[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.Weight[9+x], this.Weight[19+x], this.Weight[29+x],this.Weight[39+x], this.Weight[49+x], this.Weight[59+x],this.Weight[69+x], this.Weight[79+x], this.Weight[89+x],this.Weight[99+x], this.Weight[109+x], this.Weight[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10];

        var layout = {
          barmode: 'stack',
          height: 800,
          };

        /////////////

        var trace1_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[0+x], this.pfBeta[10+x], this.pfBeta[20+x],this.pfBeta[30+x], this.pfBeta[40+x], this.pfBeta[50+x],this.pfBeta[60+x], this.pfBeta[70+x], this.pfBeta[80+x],this.pfBeta[90+x], this.pfBeta[100+x], this.pfBeta[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[1+x], this.pfBeta[11+x], this.pfBeta[21+x],this.pfBeta[31+x], this.pfBeta[41+x], this.pfBeta[51+x],this.pfBeta[61+x], this.pfBeta[71+x], this.pfBeta[81+x],this.pfBeta[91+x], this.pfBeta[101+x], this.pfBeta[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[2+x], this.pfBeta[12+x], this.pfBeta[22+x],this.pfBeta[32+x], this.pfBeta[42+x], this.pfBeta[52+x],this.pfBeta[62+x], this.pfBeta[72+x], this.pfBeta[82+x],this.pfBeta[92+x], this.pfBeta[102+x], this.pfBeta[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[3+x], this.pfBeta[13+x], this.pfBeta[23+x],this.pfBeta[33+x], this.pfBeta[43+x], this.pfBeta[53+x],this.pfBeta[63+x], this.pfBeta[73+x], this.pfBeta[83+x],this.pfBeta[93+x], this.pfBeta[103+x], this.pfBeta[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[4+x], this.pfBeta[14+x], this.pfBeta[24+x],this.pfBeta[34+x], this.pfBeta[44+x], this.pfBeta[54+x],this.pfBeta[64+x], this.pfBeta[74+x], this.pfBeta[84+x],this.pfBeta[94+x], this.pfBeta[104+x], this.pfBeta[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[5+x], this.pfBeta[15+x], this.pfBeta[25+x],this.pfBeta[35+x], this.pfBeta[45+x], this.pfBeta[55+x],this.pfBeta[65+x], this.pfBeta[75+x], this.pfBeta[85+x],this.pfBeta[95+x], this.pfBeta[105+x], this.pfBeta[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[6+x], this.pfBeta[16+x], this.pfBeta[26+x],this.pfBeta[36+x], this.pfBeta[46+x], this.pfBeta[56+x],this.pfBeta[66+x], this.pfBeta[76+x], this.pfBeta[86+x],this.pfBeta[96+x], this.pfBeta[106+x], this.pfBeta[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[7+x], this.pfBeta[17+x], this.pfBeta[27+x],this.pfBeta[37+x], this.pfBeta[47+x], this.pfBeta[57+x],this.pfBeta[67+x], this.pfBeta[77+x], this.pfBeta[87+x],this.pfBeta[97+x], this.pfBeta[107+x], this.pfBeta[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[8+x], this.pfBeta[18+x], this.pfBeta[28+x],this.pfBeta[38+x], this.pfBeta[48+x], this.pfBeta[58+x],this.pfBeta[68+x], this.pfBeta[78+x], this.pfBeta[88+x],this.pfBeta[98+x], this.pfBeta[108+x], this.pfBeta[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfBeta[9+x], this.pfBeta[19+x], this.pfBeta[29+x],this.pfBeta[39+x], this.pfBeta[49+x], this.pfBeta[59+x],this.pfBeta[69+x], this.pfBeta[79+x], this.pfBeta[89+x],this.pfBeta[99+x], this.pfBeta[109+x], this.pfBeta[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data_2 = [trace1_2, trace2_2, trace3_2, trace4_2, trace5_2, trace6_2, trace7_2, trace8_2, trace9_2, trace10_2];

        ////////////////////////////

        var trace1_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[0+x], this.pfSysVol[10+x], this.pfSysVol[20+x],this.pfSysVol[30+x], this.pfSysVol[40+x], this.pfSysVol[50+x],this.pfSysVol[60+x], this.pfSysVol[70+x], this.pfSysVol[80+x],this.pfSysVol[90+x], this.pfSysVol[100+x], this.pfSysVol[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[1+x], this.pfSysVol[11+x], this.pfSysVol[21+x],this.pfSysVol[31+x], this.pfSysVol[41+x], this.pfSysVol[51+x],this.pfSysVol[61+x], this.pfSysVol[71+x], this.pfSysVol[81+x],this.pfSysVol[91+x], this.pfSysVol[101+x], this.pfSysVol[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[2+x], this.pfSysVol[12+x], this.pfSysVol[22+x],this.pfSysVol[32+x], this.pfSysVol[42+x], this.pfSysVol[52+x],this.pfSysVol[62+x], this.pfSysVol[72+x], this.pfSysVol[82+x],this.pfSysVol[92+x], this.pfSysVol[102+x], this.pfSysVol[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[3+x], this.pfSysVol[13+x], this.pfSysVol[23+x],this.pfSysVol[33+x], this.pfSysVol[43+x], this.pfSysVol[53+x],this.pfSysVol[63+x], this.pfSysVol[73+x], this.pfSysVol[83+x],this.pfSysVol[93+x], this.pfSysVol[103+x], this.pfSysVol[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[4+x], this.pfSysVol[14+x], this.pfSysVol[24+x],this.pfSysVol[34+x], this.pfSysVol[44+x], this.pfSysVol[54+x],this.pfSysVol[64+x], this.pfSysVol[74+x], this.pfSysVol[84+x],this.pfSysVol[94+x], this.pfSysVol[104+x], this.pfSysVol[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[5+x], this.pfSysVol[15+x], this.pfSysVol[25+x],this.pfSysVol[35+x], this.pfSysVol[45+x], this.pfSysVol[55+x],this.pfSysVol[65+x], this.pfSysVol[75+x], this.pfSysVol[85+x],this.pfSysVol[95+x], this.pfSysVol[105+x], this.pfSysVol[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[6+x], this.pfSysVol[16+x], this.pfSysVol[26+x],this.pfSysVol[36+x], this.pfSysVol[46+x], this.pfSysVol[56+x],this.pfSysVol[66+x], this.pfSysVol[76+x], this.pfSysVol[86+x],this.pfSysVol[96+x], this.pfSysVol[106+x], this.pfSysVol[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[7+x], this.pfSysVol[17+x], this.pfSysVol[27+x],this.pfSysVol[37+x], this.pfSysVol[47+x], this.pfSysVol[57+x],this.pfSysVol[67+x], this.pfSysVol[77+x], this.pfSysVol[87+x],this.pfSysVol[97+x], this.pfSysVol[107+x], this.pfSysVol[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[8+x], this.pfSysVol[18+x], this.pfSysVol[28+x],this.pfSysVol[38+x], this.pfSysVol[48+x], this.pfSysVol[58+x],this.pfSysVol[68+x], this.pfSysVol[78+x], this.pfSysVol[88+x],this.pfSysVol[98+x], this.pfSysVol[108+x], this.pfSysVol[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSysVol[9+x], this.pfSysVol[19+x], this.pfSysVol[29+x],this.pfSysVol[39+x], this.pfSysVol[49+x], this.pfSysVol[59+x],this.pfSysVol[69+x], this.pfSysVol[79+x], this.pfSysVol[89+x],this.pfSysVol[99+x], this.pfSysVol[109+x], this.pfSysVol[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data_3 = [trace1_3, trace2_3, trace3_3, trace4_3, trace5_3, trace6_3, trace7_3, trace8_3, trace9_3, trace10_3];

        /////////////////////
         var trace1_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[0+x], this.pfSpecVar[10+x], this.pfSpecVar[20+x],this.pfSpecVar[30+x], this.pfSpecVar[40+x], this.pfSpecVar[50+x],this.pfSpecVar[60+x], this.pfSpecVar[70+x], this.pfSpecVar[80+x],this.pfSpecVar[90+x], this.pfSpecVar[100+x], this.pfSpecVar[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[1+x], this.pfSpecVar[11+x], this.pfSpecVar[21+x],this.pfSpecVar[31+x], this.pfSpecVar[41+x], this.pfSpecVar[51+x],this.pfSpecVar[61+x], this.pfSpecVar[71+x], this.pfSpecVar[81+x],this.pfSpecVar[91+x], this.pfSpecVar[101+x], this.pfSpecVar[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[2+x], this.pfSpecVar[12+x], this.pfSpecVar[22+x],this.pfSpecVar[32+x], this.pfSpecVar[42+x], this.pfSpecVar[52+x],this.pfSpecVar[62+x], this.pfSpecVar[72+x], this.pfSpecVar[82+x],this.pfSpecVar[92+x], this.pfSpecVar[102+x], this.pfSpecVar[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[3+x], this.pfSpecVar[13+x], this.pfSpecVar[23+x],this.pfSpecVar[33+x], this.pfSpecVar[43+x], this.pfSpecVar[53+x],this.pfSpecVar[63+x], this.pfSpecVar[73+x], this.pfSpecVar[83+x],this.pfSpecVar[93+x], this.pfSpecVar[103+x], this.pfSpecVar[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[4+x], this.pfSpecVar[14+x], this.pfSpecVar[24+x],this.pfSpecVar[34+x], this.pfSpecVar[44+x], this.pfSpecVar[54+x],this.pfSpecVar[64+x], this.pfSpecVar[74+x], this.pfSpecVar[84+x],this.pfSpecVar[94+x], this.pfSpecVar[104+x], this.pfSpecVar[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[5+x], this.pfSpecVar[15+x], this.pfSpecVar[25+x],this.pfSpecVar[35+x], this.pfSpecVar[45+x], this.pfSpecVar[55+x],this.pfSpecVar[65+x], this.pfSpecVar[75+x], this.pfSpecVar[85+x],this.pfSpecVar[95+x], this.pfSpecVar[105+x], this.pfSpecVar[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[6+x], this.pfSpecVar[16+x], this.pfSpecVar[26+x],this.pfSpecVar[36+x], this.pfSpecVar[46+x], this.pfSpecVar[56+x],this.pfSpecVar[66+x], this.pfSpecVar[76+x], this.pfSpecVar[86+x],this.pfSpecVar[96+x], this.pfSpecVar[106+x], this.pfSpecVar[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[7+x], this.pfSpecVar[17+x], this.pfSpecVar[27+x],this.pfSpecVar[37+x], this.pfSpecVar[47+x], this.pfSpecVar[57+x],this.pfSpecVar[67+x], this.pfSpecVar[77+x], this.pfSpecVar[87+x],this.pfSpecVar[97+x], this.pfSpecVar[107+x], this.pfSpecVar[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[8+x], this.pfSpecVar[18+x], this.pfSpecVar[28+x],this.pfSpecVar[38+x], this.pfSpecVar[48+x], this.pfSpecVar[58+x],this.pfSpecVar[68+x], this.pfSpecVar[78+x], this.pfSpecVar[88+x],this.pfSpecVar[98+x], this.pfSpecVar[108+x], this.pfSpecVar[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [this.pfSpecVar[9+x], this.pfSpecVar[19+x], this.pfSpecVar[29+x],this.pfSpecVar[39+x], this.pfSpecVar[49+x], this.pfSpecVar[59+x],this.pfSpecVar[69+x], this.pfSpecVar[79+x], this.pfSpecVar[89+x],this.pfSpecVar[99+x], this.pfSpecVar[109+x], this.pfSpecVar[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data_4 = [trace1_4, trace2_4, trace3_4, trace4_4, trace5_4, trace6_4, trace7_4, trace8_4, trace9_4, trace10_4];


        // console.log(data_3)

        if (this.selectedPlot == 'Weight') {
          Plotly.newPlot('myDiv', data,layout);
        } else if (this.selectedPlot == 'Beta') {
          Plotly.newPlot('myDiv', data_2,layout);
        } else if (this.selectedPlot == 'Sysvol') {
          Plotly.newPlot('myDiv', data_3,layout);
        } else if (this.selectedPlot == 'Specvar') {
          Plotly.newPlot('myDiv', data_4,layout);
        }

        }
    },



  },



  data() {
      return {
        index: '',
        proxy: '',
        xi: '',
        trace1: {},
        IStemp: '',
        Index_Code: [],
        Date: [],
        Industry: [],
        Weight:[],
        i:'',
        isBusy: false,
        yi: '',
        IStemp1: '',
        pfBeta: [],
        pfSysVol: [],
        filterOn: [],
        pfSpecVar: [],
        previousSelection: '',
        // indexPlot = 0,

        selectedIndex: null,
        IndexOptions: [
          { value: null, text: 'Please select the index' },
          { value: 'ALSI', text: 'All Share Index (ALSI)' },
          { value: 'ALTI', text: 'Africa Alternative Index (ALTI)' },
          { value: 'FINI', text: 'Financial 15 Index (FINI)' },
          { value: 'FLED', text: 'Fledging Index (FLED)' },
          { value: 'INDI', text: 'Industrial 25 Index (INDI)' },
          { value: 'LRGC', text: 'Large Cap Index (LRGC)' },
          { value: 'MIDC', text: 'Mid Cap Index (MIDC)' },
          { value: 'PCAP', text: 'Capped Property Index (PCAP)' },
          { value: 'RESI', text: 'Resource 20 Index (RESI)' },
          { value: 'SAPY', text: 'SA Listed Property Index (SAPY)' },
          { value: 'SMLC', text: 'Small Cap Index (SMLC)' },
          { value: 'TOPI', text: 'Top 40 Index (TOPI)' },

        ],
        selectedJSE: null,
        JSEoptions: [
          { value: null, text: 'Please select the market proxy' },
          { value: 'J200', text: 'Top 40 (J200)'},
          { value: 'J203', text: 'All Share (J203)' },
          { value: 'J250', text: 'Financials and Industrials (J250)' },
          { value: 'J257', text: 'Industrials (J257)' },
          { value: 'J258', text: 'Resources (J258)' },
        ],
        selectedPlot: null,
        PlotOptions: [
          { value: null, text: 'Please select the plot required' },
          { value: 'Weight', text: 'Weight Decomposition'},
          { value: 'Beta', text: 'Beta Decomposition' },
          { value: 'Sysvol', text: 'Systematic Volatility Decomposition' },
          { value: 'Specvar', text: 'Specific Variance Decomposition' },
        ],

        fields: ['Index_Code', 'Year_Month', 'Industry','Weight','pfBeta','pfSysVol', 'pfSpecVar'],

      }


    },




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
