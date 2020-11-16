<template>
<!-- This is the home page of the dashboard -->
<div class="main">
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 id="welcome" class="h2">Welcome to the ERS Report</h1>
    </div>
      <p>
    <a class="btn" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
      This interactive dashboard is a digitised version of the AIFMRM Equity Risk Service Report. [click for more info]
    </a>
  </p>
  <div class="collapse" id="collapseExample">
    <div class="card card-body"><p>This interactive dashboard is a digitised version of the AIFMRM Equity Risk Service Report. This service is aimed at providing up-to-date risk measures and associated statistics for the stocks and indices that are listed on the Johannesburg
      Stock Exchange (JSE). </p>
    <p> The ERS report differs from others in that the estimation procedure is refined and enhanced to improve the accuracy of the risk estimates. Firstly, a thin-trading correction procedure, known as the “trade-to-trade”, is implemented to preclude
      biases in sample beta estimates caused by thin-trading. Secondly, a Bayesian adjustment is implemented which reduces estimation error by incorporating prior distributional information on sample beta estimates. Prior research by BNP has shown that
      this adjustment improves the predictability of betas by approximately 20%. </p>
</div>
  </div>

  <hr />
  <h4>Indices with largest change (Δ) in Beta</h4>
  <br>
  <!-- First table-->
  <b-table hover head-variant="dark" sticky-header="408px" outlined sort-icon-left :sort-by.sync="sortBy1" :sort-desc.sync="sortDesc1" :items="deltaBeta" :fields="fieldsTab1" :busy="isBusy1">
    <!-- Display loading animation while waiting for the data -->
    <template #table-busy>
              <div class="text-center text-danger my-2">
              <b-spinner class="align-middle"></b-spinner>
              <strong> Loading...</strong>
              </div>
    </template>
  </b-table>
  <b-row>
    <b-col sm="3" md="9" class="my-1">

    </b-col>
    <!-- Code to download CSV files, used four each table -->
    <b-col sm="3" md="3" class="my-1">
      <download-csv :data="JSON.parse(JSON.stringify(deltaBeta))" :fields="['Code','Name','J200','J203','J250','J257','J258']" :labels="{ J200:'Δ J200', J203:'Δ J203', J250:'Δ J250', J257:'Δ J257', J258:'Δ J258'}" :name="dataFile1"
        v-on:export-finished="exported">
        <b-button variant="success">Download table</b-button>
      </download-csv>
    </b-col>
  </b-row>
  <h4>Indices with largest percent change (% Δ) in Beta</h4>
  <br>
  <!-- Second table-->
  <b-table hover head-variant="dark" sticky-header="408px" outlined sort-icon-left :sort-by.sync="sortBy2" :sort-desc.sync="sortDesc2" :items="deltaBeta" :fields="fieldsTab2" :busy="isBusy2">
    <!-- Display loading animation while waiting for the data -->
    <template #table-busy>
              <div class="text-center text-danger my-2">
              <b-spinner class="align-middle"></b-spinner>
              <strong> Loading...</strong>
              </div>
    </template>
  </b-table>
  <b-row>
    <b-col sm="3" md="9" class="my-1">

    </b-col>

    <b-col sm="3" md="3" class="my-1">
      <download-csv :data="JSON.parse(JSON.stringify(deltaBeta))" :fields="['Code','Name','J200_1','J203_1','J250_1','J257_1','J258_1']" :labels="{ J200_1:'% Δ J200', J203_1:'% Δ J203', J250_1:'% Δ J250', J257_1:'% Δ J257', J258_1:'% Δ J258'}"
        :name="dataFile2" v-on:export-finished="exported">
        <b-button variant="success">Download table</b-button>
      </download-csv>
    </b-col>
  </b-row>
  <br>
  <hr />
  <div ></div>
  <h4>Shares with largest change (Δ) in Beta</h4>
  <br>
  <!-- Third table-->
  <b-table hover head-variant="dark" sticky-header="408px" outlined sort-icon-left :sort-by.sync="sortBy1" :sort-desc.sync="sortDesc1" :items="deltaShare" :fields="fieldsTab3" :busy="isBusy3">
    <!-- Display loading animation while waiting for the data -->
    <template #table-busy>
              <div class="text-center text-danger my-2">
              <b-spinner class="align-middle"></b-spinner>
              <strong> Loading...</strong>
              </div>
    </template>
  </b-table>
  <b-row>
    <b-col sm="3" md="9" class="my-1">
    </b-col>
    <b-col sm="3" md="3" class="my-1">
      <download-csv :data="JSON.parse(JSON.stringify(deltaShare))" :fields="['Code','Industry','J200','J203','J250','J257','J258']" :labels="{ J200:'Δ J200', J203:'Δ J203', J250:'Δ J250', J257:'Δ J257', J258:'Δ J258'}" :name="dataFile3"
        v-on:export-finished="exported">
        <b-button variant="success">Download table</b-button>
      </download-csv>
    </b-col>
  </b-row>
  <h4>Shares with largest percent change (% Δ) in Beta</h4>
  <br>
  <!-- Fourth table-->
  <b-table hover head-variant="dark" sticky-header="408px" outlined sort-icon-left :sort-by.sync="sortBy2" :sort-desc.sync="sortDesc2" :items="deltaShare" :fields="fieldsTab4" :busy="isBusy4">
    <!-- Display loading animation while waiting for the data -->
    <template #table-busy>
              <div class="text-center text-danger my-2">
              <b-spinner class="align-middle"></b-spinner>
              <strong> Loading...</strong>
              </div>
    </template>
  </b-table>
  <b-row>
    <b-col sm="3" md="9" class="my-1">

    </b-col>

    <b-col sm="3" md="3" class="my-1">
      <download-csv :data="JSON.parse(JSON.stringify(deltaShare))" :fields="['Code','Industry','J200_1','J203_1','J250_1','J257_1','J258_1']" :labels="{ J200_1:'% Δ J200', J203_1:'% Δ J203', J250_1:'% Δ J250', J257_1:'% Δ J257', J258_1:'% Δ J258'}"
        :name="dataFile4" v-on:export-finished="exported">
        <b-button variant="success">Download table</b-button>
      </download-csv>
    </b-col>
  </b-row>

</div>
</template>

<script>
// Import libraries
import axios from 'axios'

export default {
  name: 'FinancialDash',
  props: {
    msg: String
  },

  methods: {

    //Method used for downloading csv files
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
      deltaBeta: [], //Change in Beta for indicies
      deltaShare: [], //Change in Beta for shares
      isBusy1: true, //Table loading
      isBusy2: true, //Table loading
      isBusy3: true, //Table loading
      isBusy4: true, //Table loading
      sortBy1: "J200", //Sort
      sortDesc1: true,
      sortBy2: "J200_1",  //Sort
      sortDesc2: true,
      //File names for the four tables
      dataFile1: 'Delta_Beta_Ind.csv',
      dataFile2: 'Delta_Beta_Ind_Perc.csv',
      dataFile3: 'Delta_Beta_Share.csv',
      dataFile4: 'Delta_Beta_Share_Perc.csv',
      isExported: false, 

      //Fields for Table 1
      fieldsTab1: [{
          key: 'Code',
          sortable: true
        },
        {
          key: 'Name',
          sortable: true
        },
        {
          key: 'Series',
          sortable: true
        },
        {
          key: 'J200',
          sortable: true,
          label: "Δ J200"
        },
        {
          key: 'J203',
          sortable: true,
          label: "Δ J203"
        },
        {
          key: 'J250',
          sortable: true,
          label: "Δ J250"
        },
        {
          key: 'J257',
          sortable: true,
          label: "Δ J257"
        },
        {
          key: 'J258',
          sortable: true,
          label: "Δ J258"
        },
      ],

      //Fields for Table 2
      fieldsTab2: [{
          key: 'Code',
          sortable: true,
          label: 'Code'
        },
        {
          key: 'Name',
          sortable: true
        },
        {
          key: 'Series',
          sortable: true
        },
        {
          key: 'J200_1',
          sortable: true,
          label: "% Δ J200"
        },
        {
          key: 'J203_1',
          sortable: true,
          label: "% Δ J203"
        },
        {
          key: 'J250_1',
          sortable: true,
          label: "% Δ J250"
        },
        {
          key: 'J257_1',
          sortable: true,
          label: "% Δ J257"
        },
        {
          key: 'J258_1',
          sortable: true,
          label: "% Δ J258"
        },
      ],

      //Fields for Table 3
      fieldsTab3: [{
          key: 'Code',
          sortable: true,
          label: 'Code'
        },
        {
          key: 'Industry',
          sortable: true
        },
        {
          key: 'J200',
          sortable: true,
          label: "Δ J200"
        },
        {
          key: 'J203',
          sortable: true,
          label: "Δ J203"
        },
        {
          key: 'J250',
          sortable: true,
          label: "Δ J250"
        },
        {
          key: 'J257',
          sortable: true,
          label: "Δ J257"
        },
        {
          key: 'J258',
          sortable: true,
          label: "Δ J258"
        },
      ],

      //Fields for Table 4
      fieldsTab4: [{
          key: 'Code',
          sortable: true,
          label: 'Code'
        },
        {
          key: 'Industry',
          sortable: true
        },
        {
          key: 'J200_1',
          sortable: true,
          label: "% Δ J200"
        },
        {
          key: 'J203_1',
          sortable: true,
          label: "% Δ J203"
        },
        {
          key: 'J250_1',
          sortable: true,
          label: "% Δ J250"
        },
        {
          key: 'J257_1',
          sortable: true,
          label: "% Δ J257"
        },
        {
          key: 'J258_1',
          sortable: true,
          label: "% Δ J258"
        },
      ],


    }
  },

  async mounted() {
    //Read data for Table 1 and 2
    axios.get("https://financials.azurewebsites.net/api/Landing_Page_Indices/FetchAll")
      .then(response => {
        this.deltaBeta = response.data
        this.isBusy1 = false
        this.isBusy2 = false
      })
      .catch(function(error) {
        console.log(error);
      });

    //Read data for Table 3 and 4
    axios.get("https://financials.azurewebsites.net/api/Landing_Page_Shares/FetchAll")
      .then(response => {
        this.deltaShare = response.data
        this.isBusy3 = false
        this.isBusy4 = false
      })
      .catch(function(error) {
        console.log(error);
      });


  },


}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#welcome {
  margin-bottom: 0;
}

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
