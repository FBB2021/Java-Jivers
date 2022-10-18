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

export default {
  name: "Heatmap",
  data: function () {
    return {
      chartOptions: {
        dataLabels: {
          enabled: false,
        },
        chart: {
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
          data: this.generateData(24, {
            min: 0,
            max: 90,
          }),
        },
        {
          name: "B",
          data: this.generateData(24, {
            min: 0,
            max: 90,
          }),
        },
        {
          name: "C",
          data: this.generateData(24, {
            min: 0,
            max: 90,
          }),
        },
        {
          name: "D",
          data: this.generateData(24, {
            min: 0,
            max: 90,
          }),
        },
        {
          name: "E",
          data: this.generateData(24, {
            min: 0,
            max: 90,
          }),
        },
        {
          name: "F",
          data: this.generateData(24, {
            min: 0,
            max: 90,
          }),
        },
        {
          name: "G",
          data: this.generateData(24, {
            min: 0,
            max: 90,
          }),
        },
      ],
    };
  },
  methods: {
    generateData(count, yrange) {
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
        width: 70%;

    }

    
}
</style>