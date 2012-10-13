import QtQuick 1.0

Rectangle {
    id: mainWindow
    anchors.fill : parent
    color:"#f3f3f3"
    
    GridView {
        id: imagegrid
        model: datamodel
        anchors.fill:parent
        cellWidth:(imagegrid.width  )/ imagenum - 1
        cellHeight:imagegrid.cellWidth  * bili
        anchors.centerIn : mainWindow
        anchors.topMargin:5
       keyNavigationWraps:true
        highlightFollowsCurrentItem:true
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