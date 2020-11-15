<template>
  <div class="main">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">Client portfolio statistics</h1>
    </div>
    <p>
      On this page you can search, filter, plot and download the synthetic construction of the most important risk
      statistics from individual statistics of each index’s constituents that have been aggregated by each of the constituent’s weight in that index, respectively. The interested indices indicated by the client are the ALSI, FLED, LRGC, MIDC, SMLC, TOPI, RESI, FINI, INDI, PCAP, SAPY and ALTI indices.

    </p>
    <hr />
<div>
<b-row>
      <b-col lg="2" class="my-1">
        <p style = "margin-bottom: 0px; margin-top: 8px;">
          Select Market Proxy:
        </p>
      </b-col>


        <b-form-group>
          <b-form-select v-model="selectedJSE" :options="JSEoptions" @change="updatePlot()" class="mb-3"></b-form-select>
        </b-form-group>
</b-row>
 <b-row>

      <b-col lg="6" class="my-1">
        <b-form-group
          label="Filter:"
          label-cols-sm="3"
          label-align-sm="left"
          label-size="sm"
          label-for="filterInput"
          class="mb-0"
        >
          <b-input-group size="s">
            <b-form-input
              v-model="filter"
              type="search"
              id="filterInput"
              placeholder="Type to search..."
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>

      <b-col lg="6" class="my-1">
        <b-form-group
          label="Filter on:"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          description="Leave all unchecked to filter on all data"
          class="mb-0">
          <b-form-checkbox-group v-model="filterOn" class="mt-1">
            <b-form-checkbox  value="Index_Code">Index Code</b-form-checkbox>
            <b-form-checkbox value="Year_Month">Year Month</b-form-checkbox>
            <b-form-checkbox value="Industry">Industry</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
      </b-col>
      <br>

      <br>

      <b-col sm="1" md="2" class="my-1">

      </b-col>

      <b-col sm="2" md="3" class="my-1">
          <b-button size="sm" @click="selectAllRows">Select all rows</b-button>
      </b-col>

      <b-col sm="2" md="3" class="my-1">
          <b-button size="sm" @click="clearSelected">Clear selected rows</b-button>
      </b-col>

      <b-col sm="2" md="3" class="my-1">
         <b-button size="sm" @click="resetSort">Reset table sorting</b-button>
      </b-col>
    </b-row>

     <br>

        <div v-if="selectedJSE == 'J200'">
          <b-table ref="J200Tab" hover head-variant="dark" sticky-header="408px" outlined selectable sort-icon-left @row-selected="onRowSelected"  :filter="filter" :filter-included-fields="filterOn"  :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :items="J200" :fields="fields" :busy="isBusy">
            <template #table-busy>
              <div class="text-center text-danger my-2">
              <b-spinner class="align-middle"></b-spinner>
              <strong> Loading...</strong>
              </div>
            </template>

          <template #cell(selected)="{ rowSelected }">
            <template v-if="rowSelected">
              <span aria-hidden="true">&check;</span>
              <span class="sr-only">Selected</span>
            </template>
            <template v-else>
              <span aria-hidden="true">&nbsp;</span>
              <span class="sr-only">Not selected</span>
            </template>
          </template>
          </b-table>
        </div>

        <div v-if="selectedJSE == 'J203'">
          <b-table ref="J203Tab" hover head-variant="dark" sticky-header="405px" outlined selectable sort-icon-left @row-selected="onRowSelected" :filter="filter" :filter-included-fields="filterOn"  :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :items="J203" :fields="fields" :busy="isBusy">
          <template #cell(selected)="{ rowSelected }">
            <template v-if="rowSelected">
              <span aria-hidden="true">&check;</span>
              <span class="sr-only">Selected</span>
            </template>
            <template v-else>
              <span aria-hidden="true">&nbsp;</span>
              <span class="sr-only">Not selected</span>
            </template>
          </template>
          </b-table>
        </div>

        <div v-if="selectedJSE == 'J250'">
          <b-table ref="J250Tab" hover head-variant="dark" sticky-header="405px" outlined selectable sort-icon-left @row-selected="onRowSelected" :filter="filter" :filter-included-fields="filterOn"  :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :items="J250" :fields="fields" :busy="isBusy">
          <template #cell(selected)="{ rowSelected }">
            <template v-if="rowSelected">
              <span aria-hidden="true">&check;</span>
              <span class="sr-only">Selected</span>
            </template>
            <template v-else>
              <span aria-hidden="true">&nbsp;</span>
              <span class="sr-only">Not selected</span>
            </template>
          </template>
          </b-table>
        </div>

        <div v-if="selectedJSE == 'J257'">
          <b-table ref="J257Tab" hover head-variant="dark" sticky-header="405px" outlined selectable sort-icon-left @row-selected="onRowSelected" :filter="filter" :filter-included-fields="filterOn"  :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :items="J257" :fields="fields" :busy="isBusy">
          <template #cell(selected)="{ rowSelected }">
            <template v-if="rowSelected">
              <span aria-hidden="true">&check;</span>
              <span class="sr-only">Selected</span>
            </template>
            <template v-else>
              <span aria-hidden="true">&nbsp;</span>
              <span class="sr-only">Not selected</span>
            </template>
          </template>
          </b-table>
        </div>

        <div v-if="selectedJSE == 'J258'">
          <b-table ref="J258Tab" hover head-variant="dark" sticky-header="405px" outlined selectable sort-icon-left @row-selected="onRowSelected" :filter="filter" :filter-included-fields="filterOn"  :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :items="J258" :fields="fields" :busy="isBusy">
          <template #cell(selected)="{ rowSelected }">
            <template v-if="rowSelected">
              <span aria-hidden="true">&check;</span>
              <span class="sr-only">Selected</span>
            </template>
            <template v-else>
              <span aria-hidden="true">&nbsp;</span>
              <span class="sr-only">Not selected</span>
            </template>
          </template>
          </b-table>
        </div>

      <div v-if="selected.length">
        <download-csv
                :data="selected"
                :name="dataFile"
                v-on:export-finished="exported"
        >
            <b-button variant="success">Download selected rows</b-button>
        </download-csv>
      </div>
      <div v-else>
      <b-button disabled>Select rows to download</b-button>
      </div>

      <br>


        <div v-if="isBusy == false" class="border-top">

        <br>
        <h2>Plots for selected market proxy - {{selectedJSE}}</h2>
        <b-row>
          <div class="col-md-3">

          </div>

          <div class="col-md-3">
            <b-form-select v-model="selectedIndex" :options="IndexOptions" size="sm" class="mt-3" v-on:change="getSelectedItem"></b-form-select>
          </div>

          <div class="col-md-3">
            <b-form-select v-model="selectedPlot" :options="PlotOptions" size="sm" class="mt-3" v-on:change="getSelectedItem"></b-form-select>
          </div>

        </b-row>
           <div v-if="selectedIndex !== null" id='myDiv'></div>
        </div>

      </div>

  </div>
</template>

<script>

import axios from 'axios'
import Plotly from 'plotly.js-dist';

export default {
  name: 'FinancialDash',
  props: {
    msg: String
  },

  methods: {

      updatePlot () {
        if (this.selectedIndex !== null) {
          console.log("WORKING??")
          this.getSelectedItem()
        }
      },

      onRowSelected(items) {
        this.selected = items
      },

      resetSort() {
        this.sortBy = "Index_Code"
        this.sortDesc = false
      },

      clearSelected() {
        if (this.selectedJSE == 'J200') {
          this.$refs.J200Tab.clearSelected()
        } else if (this.selectedJSE == 'J203') {
          this.$refs.J203Tab.clearSelected()
        } else if (this.selectedJSE == 'J250') {
          this.$refs.J250Tab.clearSelected()
        } else if (this.selectedJSE == 'J257') {
          this.$refs.J257Tab.clearSelected()
        } else {
          this.$refs.J258Tab.clearSelected()
        }
      },

      selectAllRows() {

        if (this.selectedJSE == 'J200') {
          this.$refs.J200Tab.selectAllRows()
        } else if (this.selectedJSE == 'J203') {
          this.$refs.J203Tab.selectAllRows()
        } else if (this.selectedJSE == 'J250') {
          this.$refs.J250Tab.selectAllRows()
        } else if (this.selectedJSE == 'J257') {
          this.$refs.J257Tab.selectAllRows()
        } else {
          this.$refs.J258Tab.selectAllRows()
        }
      },



       getSelectedItem() { // Just a regular js function that takes 1 arg

        var x = 0
        var yi = ''
        var IStemp1 = ''

        if (this.selectedJSE == 'J200') {
          IStemp1 = this.J200
        } else if (this.selectedJSE == 'J203') {
          IStemp1 = this.J203
        } else if (this.selectedJSE == 'J250') {
          IStemp1 = this.J250
        } else if (this.selectedJSE == 'J257') {
          IStemp1 = this.J257
        } else {
          IStemp1 = this.J258
        }

        var Index_Code = []
        var Industry = []
        var Weight =[]
        var pfBeta = []
        var pfSysVol = []
        var pfSpecVar = []

          for (yi of IStemp1) {

            Index_Code.push(yi.Index_Code)
            Industry.push(yi.Industry)
            Weight.push(yi.Weight)
            pfBeta.push(yi.pfBeta)
            pfSysVol.push(yi.pfSysVol)
            pfSpecVar.push(yi.pfSpecVar)

          }



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
          y: [Weight[0+x], Weight[10+x], Weight[20+x],Weight[30+x], Weight[40+x], Weight[50+x],Weight[60+x], Weight[70+x], Weight[80+x],Weight[90+x], Weight[100+x], Weight[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[1+x], Weight[11+x], Weight[21+x],Weight[31+x], Weight[41+x], Weight[51+x],Weight[61+x], Weight[71+x], Weight[81+x],Weight[91+x], Weight[101+x], Weight[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[2+x], Weight[12+x], Weight[22+x],Weight[32+x], Weight[42+x], Weight[52+x],Weight[62+x], Weight[72+x], Weight[82+x],Weight[92+x], Weight[102+x], Weight[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[3+x], Weight[13+x], Weight[23+x],Weight[33+x], Weight[43+x], Weight[53+x],Weight[63+x], Weight[73+x], Weight[83+x],Weight[93+x], Weight[103+x], Weight[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[4+x], Weight[14+x], Weight[24+x],Weight[34+x], Weight[44+x], Weight[54+x],Weight[64+x], Weight[74+x], Weight[84+x],Weight[94+x], Weight[104+x], Weight[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[5+x], Weight[15+x], Weight[25+x],Weight[35+x], Weight[45+x], Weight[55+x],Weight[65+x], Weight[75+x], Weight[85+x],Weight[95+x], Weight[105+x], Weight[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[6+x], Weight[16+x], Weight[26+x],Weight[36+x], Weight[46+x], Weight[56+x],Weight[66+x], Weight[76+x], Weight[86+x],Weight[96+x], Weight[106+x], Weight[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[7+x], Weight[17+x], Weight[27+x],Weight[37+x], Weight[47+x], Weight[57+x],Weight[67+x], Weight[77+x], Weight[87+x],Weight[97+x], Weight[107+x], Weight[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[8+x], Weight[18+x], Weight[28+x],Weight[38+x], Weight[48+x], Weight[58+x],Weight[68+x], Weight[78+x], Weight[88+x],Weight[98+x], Weight[108+x], Weight[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [Weight[9+x], Weight[19+x], Weight[29+x],Weight[39+x], Weight[49+x], Weight[59+x],Weight[69+x], Weight[79+x], Weight[89+x],Weight[99+x], Weight[109+x], Weight[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10];

        var layout1 = {
          title: {
            text:this.selectedIndex + ' Weight for ' +this.selectedJSE,
            font: {
              family: 'Courier New, monospace',
              size: 24
            },
            xref: 'paper',
            x: 0.05,
          },
          xaxis: {
            title: {
              text: 'Date',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            },
          },
          yaxis: {
            title: {
              text: 'Weight',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            }
          },
          barmode: 'stack',
          height: 550,
          };

        /////////////

        var trace1_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[0+x], pfBeta[10+x], pfBeta[20+x],pfBeta[30+x], pfBeta[40+x], pfBeta[50+x],pfBeta[60+x], pfBeta[70+x], pfBeta[80+x],pfBeta[90+x], pfBeta[100+x], pfBeta[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[1+x], pfBeta[11+x], pfBeta[21+x],pfBeta[31+x], pfBeta[41+x], pfBeta[51+x],pfBeta[61+x], pfBeta[71+x], pfBeta[81+x],pfBeta[91+x], pfBeta[101+x], pfBeta[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[2+x], pfBeta[12+x], pfBeta[22+x],pfBeta[32+x], pfBeta[42+x], pfBeta[52+x],pfBeta[62+x], pfBeta[72+x], pfBeta[82+x],pfBeta[92+x], pfBeta[102+x], pfBeta[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[3+x], pfBeta[13+x], pfBeta[23+x],pfBeta[33+x], pfBeta[43+x], pfBeta[53+x],pfBeta[63+x], pfBeta[73+x], pfBeta[83+x],pfBeta[93+x], pfBeta[103+x], pfBeta[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[4+x], pfBeta[14+x], pfBeta[24+x],pfBeta[34+x], pfBeta[44+x], pfBeta[54+x],pfBeta[64+x], pfBeta[74+x], pfBeta[84+x],pfBeta[94+x], pfBeta[104+x], pfBeta[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[5+x], pfBeta[15+x], pfBeta[25+x],pfBeta[35+x], pfBeta[45+x], pfBeta[55+x],pfBeta[65+x], pfBeta[75+x], pfBeta[85+x],pfBeta[95+x], pfBeta[105+x], pfBeta[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[6+x], pfBeta[16+x], pfBeta[26+x],pfBeta[36+x], pfBeta[46+x], pfBeta[56+x],pfBeta[66+x], pfBeta[76+x], pfBeta[86+x],pfBeta[96+x], pfBeta[106+x], pfBeta[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[7+x], pfBeta[17+x], pfBeta[27+x],pfBeta[37+x], pfBeta[47+x], pfBeta[57+x],pfBeta[67+x], pfBeta[77+x], pfBeta[87+x],pfBeta[97+x], pfBeta[107+x], pfBeta[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[8+x], pfBeta[18+x], pfBeta[28+x],pfBeta[38+x], pfBeta[48+x], pfBeta[58+x],pfBeta[68+x], pfBeta[78+x], pfBeta[88+x],pfBeta[98+x], pfBeta[108+x], pfBeta[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10_2 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfBeta[9+x], pfBeta[19+x], pfBeta[29+x],pfBeta[39+x], pfBeta[49+x], pfBeta[59+x],pfBeta[69+x], pfBeta[79+x], pfBeta[89+x],pfBeta[99+x], pfBeta[109+x], pfBeta[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data_2 = [trace1_2, trace2_2, trace3_2, trace4_2, trace5_2, trace6_2, trace7_2, trace8_2, trace9_2, trace10_2];

        var layout2 = {
          title: {
            text:this.selectedIndex + ' Portfolio Beta for ' +this.selectedJSE,
            font: {
              family: 'Courier New, monospace',
              size: 24
            },
            xref: 'paper',
            x: 0.05,
          },
          xaxis: {
            title: {
              text: 'Date',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            },
          },
          yaxis: {
            title: {
              text: 'Portfolio Beta',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            }
          },
          barmode: 'stack',
          height: 550,
          };
        ////////////////////////////

        var trace1_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[0+x], pfSysVol[10+x], pfSysVol[20+x],pfSysVol[30+x], pfSysVol[40+x], pfSysVol[50+x],pfSysVol[60+x], pfSysVol[70+x], pfSysVol[80+x],pfSysVol[90+x], pfSysVol[100+x], pfSysVol[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[1+x], pfSysVol[11+x], pfSysVol[21+x],pfSysVol[31+x], pfSysVol[41+x], pfSysVol[51+x],pfSysVol[61+x], pfSysVol[71+x], pfSysVol[81+x],pfSysVol[91+x], pfSysVol[101+x], pfSysVol[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[2+x], pfSysVol[12+x], pfSysVol[22+x],pfSysVol[32+x], pfSysVol[42+x], pfSysVol[52+x],pfSysVol[62+x], pfSysVol[72+x], pfSysVol[82+x],pfSysVol[92+x], pfSysVol[102+x], pfSysVol[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[3+x], pfSysVol[13+x], pfSysVol[23+x],pfSysVol[33+x], pfSysVol[43+x], pfSysVol[53+x],pfSysVol[63+x], pfSysVol[73+x], pfSysVol[83+x],pfSysVol[93+x], pfSysVol[103+x], pfSysVol[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[4+x], pfSysVol[14+x], pfSysVol[24+x],pfSysVol[34+x], pfSysVol[44+x], pfSysVol[54+x],pfSysVol[64+x], pfSysVol[74+x], pfSysVol[84+x],pfSysVol[94+x], pfSysVol[104+x], pfSysVol[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[5+x], pfSysVol[15+x], pfSysVol[25+x],pfSysVol[35+x], pfSysVol[45+x], pfSysVol[55+x],pfSysVol[65+x], pfSysVol[75+x], pfSysVol[85+x],pfSysVol[95+x], pfSysVol[105+x], pfSysVol[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[6+x], pfSysVol[16+x], pfSysVol[26+x],pfSysVol[36+x], pfSysVol[46+x], pfSysVol[56+x],pfSysVol[66+x], pfSysVol[76+x], pfSysVol[86+x],pfSysVol[96+x], pfSysVol[106+x], pfSysVol[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[7+x], pfSysVol[17+x], pfSysVol[27+x],pfSysVol[37+x], pfSysVol[47+x], pfSysVol[57+x],pfSysVol[67+x], pfSysVol[77+x], pfSysVol[87+x],pfSysVol[97+x], pfSysVol[107+x], pfSysVol[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[8+x], pfSysVol[18+x], pfSysVol[28+x],pfSysVol[38+x], pfSysVol[48+x], pfSysVol[58+x],pfSysVol[68+x], pfSysVol[78+x], pfSysVol[88+x],pfSysVol[98+x], pfSysVol[108+x], pfSysVol[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10_3 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSysVol[9+x], pfSysVol[19+x], pfSysVol[29+x],pfSysVol[39+x], pfSysVol[49+x], pfSysVol[59+x],pfSysVol[69+x], pfSysVol[79+x], pfSysVol[89+x],pfSysVol[99+x], pfSysVol[109+x], pfSysVol[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data_3 = [trace1_3, trace2_3, trace3_3, trace4_3, trace5_3, trace6_3, trace7_3, trace8_3, trace9_3, trace10_3];

        var layout3 = {
          title: {
            text: this.selectedIndex + ' Portfolio Systematic Volatility for ' +this.selectedJSE,
            font: {
              family: 'Courier New, monospace',
              size: 24
            },
            xref: 'paper',
            x: 0.05,
          },
          xaxis: {
            title: {
              text: 'Date',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            },
          },
          yaxis: {
            title: {
              text: 'pfSysVol',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            }
          },
          barmode: 'stack',
          height: 550,
          };
        /////////////////////
         var trace1_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[0+x], pfSpecVar[10+x], pfSpecVar[20+x],pfSpecVar[30+x], pfSpecVar[40+x], pfSpecVar[50+x],pfSpecVar[60+x], pfSpecVar[70+x], pfSpecVar[80+x],pfSpecVar[90+x], pfSpecVar[100+x], pfSpecVar[110+x]],
          name: 'Basic Materials',
          type: 'bar'
        };

        var trace2_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[1+x], pfSpecVar[11+x], pfSpecVar[21+x],pfSpecVar[31+x], pfSpecVar[41+x], pfSpecVar[51+x],pfSpecVar[61+x], pfSpecVar[71+x], pfSpecVar[81+x],pfSpecVar[91+x], pfSpecVar[101+x], pfSpecVar[111+x]],
          name: 'Consumer Goods',
          type: 'bar'
        };

        var trace3_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[2+x], pfSpecVar[12+x], pfSpecVar[22+x],pfSpecVar[32+x], pfSpecVar[42+x], pfSpecVar[52+x],pfSpecVar[62+x], pfSpecVar[72+x], pfSpecVar[82+x],pfSpecVar[92+x], pfSpecVar[102+x], pfSpecVar[112+x]],
          name: 'Consumer Services',
          type: 'bar'
        };

        var trace4_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[3+x], pfSpecVar[13+x], pfSpecVar[23+x],pfSpecVar[33+x], pfSpecVar[43+x], pfSpecVar[53+x],pfSpecVar[63+x], pfSpecVar[73+x], pfSpecVar[83+x],pfSpecVar[93+x], pfSpecVar[103+x], pfSpecVar[113+x]],
          name: 'Financials',
          type: 'bar'
        };

        var trace5_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[4+x], pfSpecVar[14+x], pfSpecVar[24+x],pfSpecVar[34+x], pfSpecVar[44+x], pfSpecVar[54+x],pfSpecVar[64+x], pfSpecVar[74+x], pfSpecVar[84+x],pfSpecVar[94+x], pfSpecVar[104+x], pfSpecVar[114+x]],
          name: 'Health Care',
          type: 'bar'
        };

        var trace6_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[5+x], pfSpecVar[15+x], pfSpecVar[25+x],pfSpecVar[35+x], pfSpecVar[45+x], pfSpecVar[55+x],pfSpecVar[65+x], pfSpecVar[75+x], pfSpecVar[85+x],pfSpecVar[95+x], pfSpecVar[105+x], pfSpecVar[115+x]],
          name: 'Industrials',
          type: 'bar'
        };

        var trace7_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[6+x], pfSpecVar[16+x], pfSpecVar[26+x],pfSpecVar[36+x], pfSpecVar[46+x], pfSpecVar[56+x],pfSpecVar[66+x], pfSpecVar[76+x], pfSpecVar[86+x],pfSpecVar[96+x], pfSpecVar[106+x], pfSpecVar[116+x]],
          name: 'Oil & Gas',
          type: 'bar'
        };

        var trace8_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[7+x], pfSpecVar[17+x], pfSpecVar[27+x],pfSpecVar[37+x], pfSpecVar[47+x], pfSpecVar[57+x],pfSpecVar[67+x], pfSpecVar[77+x], pfSpecVar[87+x],pfSpecVar[97+x], pfSpecVar[107+x], pfSpecVar[117+x]],
          name: 'Technology',
          type: 'bar'
        };

        var trace9_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[8+x], pfSpecVar[18+x], pfSpecVar[28+x],pfSpecVar[38+x], pfSpecVar[48+x], pfSpecVar[58+x],pfSpecVar[68+x], pfSpecVar[78+x], pfSpecVar[88+x],pfSpecVar[98+x], pfSpecVar[108+x], pfSpecVar[118+x]],
          name: 'Telecommunications',
          type: 'bar'
        };

        var trace10_4 = {
          x: ['2017-Q3', '2017-Q4', '2018-Q1','2018-Q2', '2018-Q3', '2018-Q4','2019-Q1', '2019-Q2', '2019-Q3','2019-Q4', '2020-Q1', '2020-Q2'],
          y: [pfSpecVar[9+x], pfSpecVar[19+x], pfSpecVar[29+x],pfSpecVar[39+x], pfSpecVar[49+x], pfSpecVar[59+x],pfSpecVar[69+x], pfSpecVar[79+x], pfSpecVar[89+x],pfSpecVar[99+x], pfSpecVar[109+x], pfSpecVar[119+x]],
          name: 'Utilities',
          type: 'bar'
        };

        var data_4 = [trace1_4, trace2_4, trace3_4, trace4_4, trace5_4, trace6_4, trace7_4, trace8_4, trace9_4, trace10_4];
        var layout4 = {
          title: {
            text:this.selectedIndex + ' Portfolio Specific Variance for ' +this.selectedJSE,
            font: {
              family: 'Courier New, monospace',
              size: 24
            },
            xref: 'paper',
            x: 0.05,
          },
          xaxis: {
            title: {
              text: 'Date',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            },
          },
          yaxis: {
            title: {
              text: 'pfSpecVar',
              font: {
                family: 'Courier New, monospace',
                size: 18,
              }
            }
          },
          barmode: 'stack',
          height: 550,
          };

        // console.log(data_3)

        if (this.selectedPlot == 'Weight') {
          //console.log("PLOT DATA")
          //console.log(data)
          Plotly.newPlot('myDiv', data,layout1);
        } else if (this.selectedPlot == 'Beta') {
          Plotly.newPlot('myDiv', data_2,layout2);
        } else if (this.selectedPlot == 'Sysvol') {
          Plotly.newPlot('myDiv', data_3,layout3);
        } else if (this.selectedPlot == 'Specvar') {
          Plotly.newPlot('myDiv', data_4,layout4);
        }


      },

      exported(event) {
        console.log(event)
        this.isExported = true
        setTimeout(() => {
          this.isExported = false
        }, 3 * 1000)
      },




  },

  data() {
      return {
        isBusy: true,
        J200: [],
        J203: [],
        J250: [],
        J257: [],
        J258: [],
        selected: [],
        sortBy: 'Index_Code',
        sortDesc: false,
        filter: null,
        filterOn: [],
        JSEOption: 'J200',
        dataFile: 'Client_Indicies.csv',
        isExported: false,


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
        selectedJSE: 'J200',
        JSEoptions: [
          { value: 'J200', text: 'Top 40 (J200)'},
          { value: 'J203', text: 'All Share (J203)' },
          { value: 'J250', text: 'Financials and Industrials (J250)' },
          { value: 'J257', text: 'Industrials (J257)' },
          { value: 'J258', text: 'Resources (J258)' },
        ],
        selectedPlot: 'Weight',
        PlotOptions: [
          { value: 'Weight', text: 'Weight Decomposition'},
          { value: 'Beta', text: 'Beta Decomposition' },
          { value: 'Sysvol', text: 'Systematic Volatility Decomposition' },
          { value: 'Specvar', text: 'Specific Variance Decomposition' },
        ],

        selectedStart: null,
        startOptions: [
          { value: null, text: 'Select year' },
          { value: "2017", text: '2017' },
          { value: "2018", text: '2018' },
          { value: "2019", text: '2019' },
          { value: "2020", text: '2020' },

        ],

        selectedEnd: null,
        endOptions: [
          { value: null, text: 'Select year' },
          { value: "2017", text: '2017' },
          { value: "2018", text: '2018' },
          { value: "2019", text: '2019' },
          { value: "2020", text: '2020' },
        ],

        fields: [{key: 'Index_Code', sortable: true},
        {key: 'Year_Month', sortable: true},
        {key: 'Industry', sortable: true},
        {key: 'Weight', sortable: true},
        {key: 'pfBeta', sortable: true},
        {key: 'pfSysVol', sortable: true},
        {key: 'pfSpecVar', sortable: true},
        'selected'],

      }


    },

    async mounted () {

      axios.get("http://financials.azurewebsites.net/api/J200/FetchAll")
          .then(response => {
              this.J200 = response.data
              //console.log(response.data)
              this.isBusy = false
          })
        .catch(function (error) {
              console.log(error);
      });

      axios.get("http://financials.azurewebsites.net/api/J203/FetchAll")
          .then(response => {
              this.J203 = response.data
          })
        .catch(function (error) {
              console.log(error);
      });

      axios.get("http://financials.azurewebsites.net/api/J250/FetchAll")
          .then(response => {
              this.J250 = response.data
          })
        .catch(function (error) {
              console.log(error);
      });

      axios.get("http://financials.azurewebsites.net/api/J257/FetchAll")
          .then(response => {
              this.J257 = response.data
          })
        .catch(function (error) {
              console.log(error);
      });

      axios.get("http://financials.azurewebsites.net/api/J258/FetchAll")
          .then(response => {
              this.J258 = response.data
          })
        .catch(function (error) {
              console.log(error);
      });

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
