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
                    data: this.generateData(10, {
                        min: 0,
                        max: 21,
                    }),
                },
                {
                    name: "B",
                    data: this.generateData(10, {
                        min: 0,
                        max: 21,
                    }),
                },
                {
                    name: "C",
                    data: this.generateData(10, {
                        min: 0,
                        max: 21,
                    }),
                },
                {
                    name: "D",
                    data: this.generateData(10, {
                        min: 0,
                        max: 21,
                    }),
                },
            ],
        };
    },
    mounted() {},
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
            console.log(series);
            return series;
        },
    },
};
</script>

<style lang="scss">
.data-view {
    width: 100%;
    display: flex;
    justify-content: space-between;
    .el-card {
        width: 75%;
    }
}
</style>
