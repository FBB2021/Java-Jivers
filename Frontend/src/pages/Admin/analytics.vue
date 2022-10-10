<template>
    <div class="content">
        <div class="data-view">
            <el-card>
                <div id="graph1">

                </div>
            </el-card>
            <el-card>
                <div id="graph2">
                    
                </div>
            </el-card>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{

        }
    },
    mounted(){
        let myChart = this.$echarts.init(document.getElementById('graph1'))
        myChart.setOption({
            title: {
                text: 'Graph of stock level'
            },
            tooltip:{},
            xAxis:{
                data:[]
            }
        })
    }

};
</script>
<style lang="scss">
.data-view{
    width: 100%;
    display: flex;
    justify-content: space-between;
    .el-card{
        width: 50%;
        #graph1,#graph2{
            height: 500px;
        }
    }
}
</style>
