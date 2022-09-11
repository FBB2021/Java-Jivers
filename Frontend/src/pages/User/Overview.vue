<!-- This is the homepage -->

<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-20">
          <base-input type="text"
                      label="Search"
                      :disabled="false"
                      placeholder="Try typeing 'new'"
                      v-model="model">
          </base-input>
        </div>
      </div>


    </div>
  </div>
</template>
<script>
  import ChartCard from 'src/components/Cards/ChartCard.vue'
  import StatsCard from 'src/components/Cards/StatsCard.vue'
  import LTable from 'src/components/Table.vue'

  export default {
    components: {
      LTable,
      ChartCard,
      StatsCard
    },
    data () {
      return {
        editTooltip: 'Edit Task',
        deleteTooltip: 'Remove',
        pieChart: {
          data: {
            labels: ['40%', '20%', '40%'],
            series: [40, 20, 40]
          }
        },
        lineChart: {
          data: {
            // need to get data from the database
            labels: ['25/08', '26/08', '27/08', '28/08', '29/08', '30/08', '31/08', '01/09'],
            series: [
              [287, 385, 490, 492, 554, 586, 698, 695],
              [67, 152, 143, 240, 287, 335, 435, 437],
              [23, 113, 67, 108, 190, 239, 307, 308]
            ]
          },
          options: {
            low: 0,
            high: 800,
            showArea: false,
            height: '245px',
            axisX: {
              showGrid: false
            },
            lineSmooth: true,
            showLine: true,
            showPoint: true,
            fullWidth: true,
            chartPadding: {
              right: 50
            }
          },
          responsiveOptions: [
            ['screen and (max-width: 640px)', {
              axisX: {
                labelInterpolationFnc (value) {
                  return value[0]
                }
              }
            }]
          ]
        },
        barChart: {
          data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            series: [
              [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895],
              [412, 243, 280, 580, 453, 353, 300, 364, 368, 410, 636, 695]
            ]
          },
          options: {
            seriesBarDistance: 10,
            axisX: {
              showGrid: false
            },
            height: '245px'
          },
          responsiveOptions: [
            ['screen and (max-width: 640px)', {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc (value) {
                  return value[0]
                }
              }
            }]
          ]
        },
        // tableData: {
        //   data: [
        //     {title: 'Sign contract for "What are conference organizers afraid of?"', checked: false},
        //     {title: 'Lines From Great Russian Literature? Or E-mails From My Boss?', checked: true},
        //     {
        //       title: 'Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit',
        //       checked: true
        //     },
        //     {title: 'Create 4 Invisible User Experiences you Never Knew About', checked: false},
        //     {title: 'Read "Following makes Medium better"', checked: false},
        //     {title: 'Unfollow 5 enemies from twitter', checked: false}
        //   ]
        // }
      }
    }
  }
</script>
<style>

</style>
