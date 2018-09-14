window.mobilecheck = function() {
  var check = false;
  (function(a){if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4))) check = true;})(navigator.userAgent||navigator.vendor||window.opera);
  return check;
};
var rooms = [
    {id: 1, text: "Hall", color: "#848990"},
    {id: 2, text: "Room A", color: "#2CB8AE"},
    {id: 3, text: "Room B", color: "#8F9C4C"},
    {id: 4, text: "Room C", color: "#2B78C4"}
];
var resources = [
    {
        fieldExpr: 'roomId',
        dataSource: rooms,
        allowMultiple: false
    }
];
var speeches = [
    {
        roomId: 1,
        text: "등록",
        speaker: "",
        startDate: new Date(2018, 10, 7, 10, 0),
        endDate: new Date(2018, 10, 7, 11, 0),
        isFull: true
    },
    {
        roomId: 2,
        text: "운영진 소개",
        speaker: "운영진",
        startDate: new Date(2018, 10, 7, 11, 0),
        endDate: new Date(2018, 10, 7, 11, 30),
        isFull: true
    },
    {
        roomId: 2,
        text: "이정윤님 발표",
        speaker: "이정윤님",
        startDate: new Date(2018, 10, 7, 11, 30),
        endDate: new Date(2018, 10, 7, 12, 30),
        isFull: true
    },
    {
        roomId: 1,
        text: "식사&네트워킹",
        speaker: "",
        startDate: new Date(2018, 10, 7, 12, 30),
        endDate: new Date(2018, 10, 7, 13, 30),
        isFull: true
    },
    {
        roomId: 2,
        text: "정권우님 발표 정권우님 발표 정권우님 발표 정권우님 발표 정권우님 발표 정권우님 발표",
        speaker: "정권우님",
        startDate: new Date(2018, 10, 7, 13, 30),
        endDate: new Date(2018, 10, 7, 14, 0),
        isFull: false
    },
    {
        roomId: 3,
        text: "강규영님 발표",
        speaker: "강규영님",
        startDate: new Date(2018, 10, 7, 13, 30),
        endDate: new Date(2018, 10, 7, 14, 0),
        isFull: false
    },
    {
        roomId: 3,
        text: "최동근님 발표",
        speaker: "최동근님",
        startDate: new Date(2018, 10, 7, 14, 0),
        endDate: new Date(2018, 10, 7, 14, 30),
        isFull: false
    },
    {
        roomId: 4,
        text: "박준용님 발표",
        speaker: "박준용님",
        startDate: new Date(2018, 10, 7, 13, 30),
        endDate: new Date(2018, 10, 7, 14, 30),
        isFull: false
    },
    {
        roomId: 1,
        text: "휴식시간",
        speaker: "박준용님",
        startDate: new Date(2018, 10, 7, 14, 30),
        endDate: new Date(2018, 10, 7, 14, 50),
        isFull: true
    },
    {
        roomId: 2,
        text: "이유한님 발표",
        speaker: "이유한님",
        startDate: new Date(2018, 10, 7, 14, 50),
        endDate: new Date(2018, 10, 7, 15, 20),
        isFull: false
    }
];
$(function () {
    $("#scheduler").dxScheduler({
        dataSource: speeches,
        resources: resources,
        currentDate: new Date(2018, 10, 7, 10, 0),
        startDayHour: 10,
        endDayHour: 18,
        currentView: window.mobilecheck() ? "agenda" : "day",
        views: [{
                    type: "day",
                    groups: ['roomId'],
                    groupOrientation: "horizontal",
                    appointmentTemplate: function(data, index, element) {
                        if (data.isFull){
                            setTimeout(() => {
                              var w = $(".dx-scheduler-date-table-cell").width();
                              element.parent().css("width", w*(4-data.roomId+1)+((4-data.roomId+1)*2));
                            });
                        } else{
                            setTimeout(() => {
                              var w = $(".dx-scheduler-date-table-cell").width();
                              element.parent().css("width", w);
                            });
                        }
                        return "item";
                    }
                }, {
                    type: "agenda",
                    groupOrientation: "horizontal"
                }
            ],
        appointmentTooltipTemplate: function (data, element) {
            element.append("<i>" + data.text + "(" + rooms[data.roomId-1].text + ")</i>");
            element.append("<p><img style='height: 80px' src='" + data.speaker + "' /></p>");
        },
        editing: {
            allowAdding: false,
            allowDeleting: false,
            allowDragging: false,
            allowResizing: false,
            allowUpdating: false
        }
    });
});