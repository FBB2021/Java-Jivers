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
import Axios from "axios";
const backendUrl = "https://java-jivers-ims.herokuapp.com/item";

export default {
    data(){
        return{
            tableData: [],
            name: ['Apple','Mango','iKiwi','Pluots','Kpwi plus','Rambutam','omni-Apple','Manuo','Pluors','Kiwi','Orange'],
            quantity:[439,915,219,333,45,315,930,399,85,640,564],
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
                data: this.name
                // data:this.tableData.name
            },
            yAxis:{},
            series:[{
                name: 'quantit',
                type: 'bar',
                // data:this.tableData.quantity
                data: this.quantity
            }]
        })
    },
    created() {
        // Axios.get(backendUrl).then((response) => {
        //         this.tableData = response.data;
        //         this.name = response.data.name
        //         this.quantity = response.data.quantity
        //         console.log(this.tableData)
        //         console.log(this.quantity)
        //     });

}
}

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
