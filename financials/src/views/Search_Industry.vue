<template>
<div class="main">
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Search by Index Code</h1>
  </div>
  <p>
  On this page you can search, view, filter, plot and download the modified Capital Asset Pricing Model (CAPM) beta of each index with respect to the FTSE/JSE’s: (i) All Share (J203); (ii) Top 40 (J200); (iii) Financials and Industrials (J250);
  (iv) Industrials (J257); and (v) Resources (J258) indices.
  </p>

  <hr />


  <b-row>

    <b-col lg="2" class="my-1">
      <p style = "margin-bottom: 0px; margin-top: 10px;">
        Filter from year:
      </p>
    </b-col>

    <b-col lg="2" class="my-1">
      <b-form-group >
        <b-form-select v-model="selectedStart" :options="startOptions" @change="filterVarThree = selectedStart" class="mb-3"></b-form-select>
      </b-form-group>
    </b-col>

    <b-col lg="2" class="my-1">
      <p style = "margin-bottom: 0px; margin-top: 10px;">
        Filter to year:
      </p>
    </b-col>

    <b-col lg="2" class="my-1">
      <b-form-group>
        <b-form-select v-model="selectedEnd" :options="endOptions" @change="filterVarFour = selectedEnd" class="mb-3"></b-form-select>
      </b-form-group>
    </b-col>

  </b-row>

  <div>


    <b-form-group label="Select the industry series:" label-cols-md="2">
      <b-form-select v-model="selectedIndus" :options="IndusOptions" @change="filterVarOne = selectedIndus" class="mb-3"></b-form-select>
    </b-form-group>


    <b-row>


      <b-col lg="8" class="my-1">
        <b-form-group label="Filter by Code:" label-cols-sm="3" label-align-sm="left" label-size="sm" label-for="filterInput" class="mb-0">
          <b-input-group size="sm">
            <b-form-input v-model="filterVarTwo" type="search" id="filterInput" placeholder="Type to search..."></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filterVarTwo" @click="filterVarTwo = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>

      <div v-if="anyfilter == true">
        <b-button variant="danger" @click="resetFiltering">Reset all filters</b-button>
      </div>
      <div v-else>
        <b-button disabled>Reset all filters</b-button>
      </div>
    </b-row>

    <br>

    <b-row>
      <b-col sm="3" md="2" class="my-1">

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

    <div>
      <b-table ref="IndiceTab" hover head-variant="dark" sticky-header="408px" outlined selectable sort-icon-left empty-filtered-html @row-selected="onRowSelected" :filter="filter" :filter-function="filterTable" :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc" :items="ShareBeta" :fields="fields" :busy="isBusy">


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


    <b-row>
      <b-col sm="3" md="1" class="my-1">

      </b-col>
      <b-col sm="3" md="4" class="my-1">
        <div v-if="selected.length && filterVarTwo.length == 4">
          <b-button lg="4" variant="success" @click="instrumentPlot">Generate/ update plot</b-button>
        </div>
        <div v-else>
          <b-button lg="4" disabled>Select instrument to generate plot</b-button>
        </div>
      </b-col>

      <b-col sm="3" md="3" class="my-1">

      </b-col>

      <b-col sm="3" md="3" class="my-1">
        <div v-if="selected.length">
          <download-csv :data="selected" :name="dataFile" v-on:export-finished="exported">
            <b-button variant="success">Download selected rows</b-button>
          </download-csv>
        </div>
        <div v-else>
          <b-button disabled>Select rows to download</b-button>
        </div>
      </b-col>

    </b-row>


  </div>
  <div id='myDiv'></div>

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

    instrumentPlot() {

      var yi = ''
      var IStemp1 = ''
      var Year_Plot = []
      var Beta_J200_Plot = []
      var Beta_J203_Plot = []
      var Beta_J250_Plot = []
      var Beta_J257_Plot = []
      var Beta_J258_Plot = []

      IStemp1 = this.selected

      for (yi of IStemp1) {
        Year_Plot.push(yi.Year_Month)
        Beta_J200_Plot.push(yi.Beta_J200)
        Beta_J203_Plot.push(yi.Beta_J203)
        Beta_J250_Plot.push(yi.Beta_J250)
        Beta_J257_Plot.push(yi.Beta_J257)
        Beta_J258_Plot.push(yi.Beta_J258)
      }

      console.log(Year_Plot)

      var trace1 = {
        x: Year_Plot,
        y: Beta_J200_Plot,
        name: 'Beta_J200',
        type: 'scatter'
      };

      console.log(Beta_J203_Plot)
      var trace2 = {
        x: Year_Plot,
        y: Beta_J203_Plot,
        name: 'Beta_J203',
        type: 'scatter'
      };

      var trace3 = {
        x: Year_Plot,
        y: Beta_J250_Plot,
        name: 'Beta_J250',
        type: 'scatter'
      };

      var trace4 = {
        x: Year_Plot,
        y: Beta_J257_Plot,
        name: 'Beta_J257',
        type: 'scatter'
      };

      var trace5 = {
        x: Year_Plot,
        y: Beta_J258_Plot,
        name: 'Beta_J258',
        type: 'scatter'
      };

      var data = [trace1, trace2, trace3, trace4, trace5];

      var layout = {
        title: {
          text: 'Beta values for ' + this.filterVarTwo + ' from ' + Year_Plot[0] + ' to ' + Year_Plot[Year_Plot.length - 1],
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
            text: 'Beta',
            font: {
              family: 'Courier New, monospace',
              size: 18,
            }
          }
        },
      };

      Plotly.newPlot('myDiv', data, layout);
    },

    onRowSelected(items) {
      this.selected = items
    },

    resetSort() {
      this.sortBy = "Year_Month"
      this.sortDesc = false
    },

    clearSelected() {

      this.$refs.IndiceTab.clearSelected()

    },

    selectAllRows() {

      this.$refs.IndiceTab.selectAllRows()

    },

    filterTable: function(tableRow, filter) {

      if (filter[0] !== null && filter[1] !== null && filter[2] !== null && filter[3] !== null) {
        //all filters set
        return tableRow.Series == filter[0] && tableRow.Instrument == filter[1] && (tableRow.Year_Month.slice(0, 4) >= filter[2] && tableRow.Year_Month.slice(0, 4) <= filter[3]);
      } else if (filter[0] !== null && filter[1] !== null && filter[2] == null && filter[3] !== null) {
        return tableRow.Series == filter[0] && tableRow.Instrument == filter[1] && tableRow.Year_Month.slice(0, 4) <= filter[3];
      } else if (filter[0] !== null && filter[1] !== null && filter[2] !== null && filter[3] == null) {
        return tableRow.Series == filter[0] && tableRow.Instrument == filter[1] && tableRow.Year_Month.slice(0, 4) >= filter[2];
      } else if (filter[0] !== null && filter[1] == null && (filter[2] !== null || filter[3] !== null)) {
        if (filter[0] !== null && filter[2] !== null && filter[3] !== null) {
          return tableRow.Series == filter[0] && (tableRow.Year_Month.slice(0, 4) >= filter[2] && tableRow.Year_Month.slice(0, 4) <= filter[3]);
        } else if (filter[2] == null && filter[3] !== null) {
          return tableRow.Series == filter[0] && tableRow.Year_Month.slice(0, 4) <= filter[3];
        }
        return tableRow.Series == filter[0] && tableRow.Year_Month.slice(0, 4) >= filter[2];
      } else if (filter[0] == null && filter[1] !== null && (filter[2] !== null || filter[3] !== null)) {
        if (filter[1] !== null && filter[2] !== null && filter[3] !== null) {
          return tableRow.Instrument == filter[1] && (tableRow.Year_Month.slice(0, 4) >= filter[2] && tableRow.Year_Month.slice(0, 4) <= filter[3]);
        } else if (filter[2] == null && filter[3] !== null) {
          return tableRow.Instrument == filter[1] && tableRow.Year_Month.slice(0, 4) <= filter[3];
        }
        return tableRow.Instrument == filter[1] && tableRow.Year_Month.slice(0, 4) >= filter[2];
      } else if (filter[0] !== null && filter[1] !== null) {
        return tableRow.Series == filter[0] && tableRow.Instrument == filter[1]
      } else if (filter[2] !== null && filter[3] !== null) {
        return tableRow.Year_Month.slice(0, 4) >= filter[2] && tableRow.Year_Month.slice(0, 4) <= filter[3]
      } else if (filter[0] !== null) {
        return tableRow.Series == filter[0]
      } else if (filter[1] !== null) {
        return tableRow.Instrument == filter[1]
      } else if (filter[2] !== null) {
        return tableRow.Year_Month.slice(0, 4) >= filter[2]
      }
      return tableRow.Year_Month.slice(0, 4) <= filter[3];

    },

    exported(event) {
      console.log(event)
      this.isExported = true
      setTimeout(() => {
        this.isExported = false
      }, 3 * 1000)
    },

    resetFiltering() {
      this.selectedIndus = null;
      this.selectedStart = null;
      this.selectedEnd = null;
      this.filterVarOne = null
      this.filterVarTwo = null
      this.filterVarThree = null
      this.filterVarFour = null
      this.anyfilter = false
    },




  },

  data() {
    return {
      isBusy: true,
      ShareBeta: [],
      selected: [],
      sortBy: 'Year_Month',
      sortDesc: false,
      filterVarOne: null,
      filterVarTwo: null,
      filterVarThree: null,
      filterVarFour: null,
      dataFile: 'Indice_Beta.csv',
      isExported: false,
      anyfilter: false,
      testvar: true,

      selectedIndus: null,
      IndusOptions: [{
          value: null,
          text: 'Please select the industry series'
        },
        {
          value: 'All Africa Index Series',
          text: '	All Africa Index Series'
        },
        {
          value: 'Dividend Forecast Index Series',
          text: 'Dividend Forecast Index Series'
        },
        {
          value: 'Equally Weighted Top 40',
          text: 'Equally Weighted Top 40'
        },
        {
          value: 'FTSE/JSE Preference Share',
          text: 'FTSE/JSE Preference Share'
        },
        {
          value: 'Headline Index',
          text: 'Headline Index'
        },
        {
          value: 'Headline Index Variants Index Series',
          text: 'Headline Index Variants Index Series'
        },
        {
          value: 'ICB Industry Index Series',
          text: 'ICB Industry Index Series'
        },
        {
          value: 'ICB Sector Index Series',
          text: '	ICB Sector Index Series'
        },
        {
          value: 'ICB Sub-Sector Index Series',
          text: 'ICB Sub-Sector Index Series'
        },
        {
          value: 'JN51',
          text: 'JN51'
        },
        {
          value: 'JNS4',
          text: 'JNS4'
        },
        {
          value: 'RAFI Index Series',
          text: 'RAFI Index Series'
        },
        {
          value: 'Responsible Investment Top 30 Series',
          text: 'Responsible Investment Top 30 Series'
        },
        {
          value: 'Secondary Market Index Series',
          text: 'Secondary Market Index Series'
        },
        {
          value: 'Shareholder Weighted (SWIX) Index Series',
          text: 'Shareholder Weighted (SWIX) Index Series'
        },
        {
          value: 'Shariah Index Series',
          text: 'Shariah Index Series'
        },
        {
          value: 'Specialist Indices Index Series',
          text: 'Specialist Indices Index Series'
        },
        {
          value: 'Specialist Property Index Series',
          text: 'Specialist Property Index Series'
        },
        {
          value: 'Style (Value and Growth) Index Series',
          text: 'Style (Value and Growth) Index Series'
        },
      ],

      selectedStart: null,
      startOptions: [{
          value: null,
          text: 'Select year'
        },
        {
          value: "2017",
          text: '2017'
        },
        {
          value: "2018",
          text: '2018'
        },
        {
          value: "2019",
          text: '2019'
        },
        {
          value: "2020",
          text: '2020'
        },

      ],

      selectedEnd: null,
      endOptions: [{
          value: null,
          text: 'Select year'
        },
        {
          value: "2017",
          text: '2017'
        },
        {
          value: "2018",
          text: '2018'
        },
        {
          value: "2019",
          text: '2019'
        },
        {
          value: "2020",
          text: '2020'
        },
      ],

      fields: [{
          key: 'Instrument',
          sortable: true,
          label: 'Code'
        },
        {
          key: 'Name',
          sortable: true
        },
        {
          key: 'Year_Month',
          sortable: true
        },
        {
          key: 'Series',
          sortable: true
        },
        {
          key: 'Data_Points',
          sortable: true
        },
        {
          key: 'Beta_J200',
          sortable: true
        },
        {
          key: 'Beta_J203',
          sortable: true
        },
        {
          key: 'Beta_J250',
          sortable: true
        },
        {
          key: 'Beta_J257',
          sortable: true
        },
        {
          key: 'Beta_J258',
          sortable: true
        },
        'selected'
      ],

    }


  },

  async mounted() {

    axios.get("https://financials.azurewebsites.net/api/Indice_Beta_Data/FetchAll")
      .then(response => {
        this.ShareBeta = response.data
        //console.log(response.data)
        this.isBusy = false
      })
      .catch(function(error) {
        console.log(error);
      });

  },

  computed: {
    filter: function() {

      if (this.filterVarTwo == '') {
        this.filterVarTwo = null

      }

      if (this.filterVarOne === null && this.filterVarTwo === null && this.filterVarThree === null && this.filterVarFour === null) {
        this.anyfilter = false;
        return null;
      } else {
        this.anyfilter = true;
        return [this.filterVarOne, this.filterVarTwo, this.filterVarThree, this.filterVarFour];
      }


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

.headingcustomtable {
  color: rgba(30, 113, 184, 1);
}
</style>
