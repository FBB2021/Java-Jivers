<template>
    <div class="content">
      <div class="data-view">
            <el-card>
              <apexchart
    type="heatmap"
    :options="chartOptions"
    :series="series"
  ></apexchart>
            </el-card>
          </div>
</div>
</template>

<script>
import Axios from "axios";
const backendUrl = "https://java-jivers-ims.herokuapp.com/item";


export default {

  name: "Heatmap",
  data: function () {
    return {
      chartOptions: {
        dataLabels: {
          enabled: false,
          tableData: []
        },
        chart: {
        

          // background: '#008FFB',
          toolbar: {
            show: false,
          },
        },
        
        colors: ["#008FFB"],
        xaxis: {
          type: "category",
        },
      },
      series: [
        {
          name: "A",
          data: this.generateDataA(10, {
            min: 0,
            max: 0,
          }),
        },
        {
          name: "B",
          data: this.generateDataB(10, {
            min: 0,
            max: 0,
          }),
        },
        {
          name: "C",
          data: this.generateDataC(10, {
            min: 0,
            max: 0,
          }),
        },
        {
          name: "D",
          data: this.generateDataD(10, {
            min: 0,
            max: 0,
          }),
        },
      ],
    };
  },
  async mounted(){
        await Axios.get(backendUrl).then((response) => {
                this.tableData = response.data;
            });

            console.log(this.tableData)
          },
  methods: {

    generateDataA(count, yrange) {
      console.log("tada!")
      console.log(this.tableData)
      // var i = 0;
      // var series = [];
      // while (i < count) {
      //   var x = `${i}`.toString();

      //   console.log("A"+x == "A1")
      //   for (var i = 0; i < this.tableData.length; i++) {
      //           if( "A"+x == this.tableData[i].nameLocation){
      //             var y = this.tableData[i].quantity
      //           }else{
      //             var y =
      //             Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
      //             yrange .min;
      //           }
      //       }


      //   series.push({
      //     x: x,
      //     y: y,
      //   });
      //   i++;
      // }
      // console.log(series)
      // return series;
    },
    generateDataB(count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {

        var x = `${i}`.toString();
        var y =
          Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
          yrange.min;

        series.push({
          x: x,
          y: y,
        });
        i++;
      }
      console.log(series)
      return series;
    },
    generateDataC(count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {

        var x = `${i}`.toString();
        var y =
          Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
          yrange.min;

        series.push({
          x: x,
          y: y,
        });
        i++;
      }
      console.log(series)
      return series;
    },
    generateDataD(count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {

        var x = `${i}`.toString();
        var y =
          Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
          yrange.min;

        series.push({
          x: x,
          y: y,
        });
        i++;
      }
      console.log(series)
      return series;
    },
  },
};
</script>

<style lang="scss">
.data-view{
    width: 100%;
    display: flex;
    justify-content: space-between;
    .el-card{
        width: 75%;
    }

    
}
</style>