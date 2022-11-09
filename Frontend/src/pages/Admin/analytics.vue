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
            tableData: ["Test"],
            name: ['Apple','Mango','iKiwi','Pluots','Kpwi plus','Rambutam','omni-Apple','Manuo','Pluors','Kiwi','Orange'],
            quantity:[439,915,219,333,45,315,930,399,85,640,564],
            names: [],
            quantities: []
        }
    },
    async mounted(){
        await Axios.get(backendUrl).then((response) => {
                this.tableData = response.data;
            });

             for (var i = 0; i < this.tableData.length; i++) {
                this.names.push(this.tableData[i].name)
                this.quantities.push(this.tableData[i].quantity)
            }
            console.log("Mounted!")
            console.log(this.tableData)
            console.log(this.names)


        let myChart = this.$echarts.init(document.getElementById('graph1'))
        myChart.setOption({
            title: {
                text: 'Graph of stock level'
            },
            tooltip:{},
            xAxis:{
                data: this.names
                // data:this.tableData.name
            },
            yAxis:{},
            series:[{
                name: 'quantity',
                type: 'bar',
                // data:this.tableData.quantity
                data: this.quantities
            }]
        })

        let myChart1 = this.$echarts.init(document.getElementById('graph2'))
        myChart1.setOption({
            title:{
                text: 'Pie Chart of Venders'
            },
            tooltip: {},
            series: [
    {
      type: 'pie',
      data: [
        {
          value: 335,
          name: 'BigW'
        },
        {
          value: 234,
          name: 'Woolworth'
        },
        {
          value: 1548,
          name: 'Apple'
        },
        {
            value: 100,
            name: "Ka Ming Industrial Limited"
        },{
            value: 2,
            name: 'Ninetendo'
        }
      ],
      radius: '50%'
    }
  ]
        })

    },
// created(){
//     console.log("Created!")
// }
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
