import QtQuick 1.0
import "randombg.js" as Random
Rectangle {
    id: mainWindow
    anchors.fill : parent
    color:"#D8D8D8"
    
    ColorBar{
        width:parent.width
        height:45
    }

    GridView {
        id: imagegrid
        model: datamodel
        anchors.fill:parent
        cellWidth:(imagegrid.width  )/ imagenum - 1
        cellHeight:imagegrid.cellWidth  * bili
        anchors.centerIn : mainWindow
        anchors.topMargin:5
        delegate: picture_component
               onFlickEnded: {
            controller.nextPage()
        }
    
        

        Component {
                id:picture_component

                Rectangle{
                    id:skin_cup
                    width:imagegrid.cellWidth
                    height:imagegrid.cellHeight
                    color:"transparent"

                    CustomImage{
                        id:picturecup
                    }
             }
        }


        
        
     }
 }