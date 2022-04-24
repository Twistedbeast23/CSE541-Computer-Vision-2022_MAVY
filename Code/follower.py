import math

class track:
    def __init__(initialize):
        initialize.mid_pts = {}
        initialize.cnt = 0


    def update(initialize, objects_rect):
        obj_boxes_ids = []
        for rect in objects_rect:
            value_x, value_y, value_width, value_height, index = rect
            cx = (value_x + value_x + value_width) // 2
            cy = (value_y + value_y + value_height) // 2
            repeated_vehical = False
            for id, pt in initialize.mid_pts.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    initialize.mid_pts[id] = (cx, cy)
                    obj_boxes_ids.append([value_x, value_y, value_width, value_height, id, index])
                    repeated_vehical = True
                    break            
            if repeated_vehical is False:
                initialize.mid_pts[initialize.cnt] = (cx, cy)
                obj_boxes_ids.append([value_x, value_y, value_width, value_height, initialize.cnt, index])
                initialize.cnt += 1
        new_mid_pts = {}
        for obj_bb_id in obj_boxes_ids:
            _, _, _, _, object_id, index = obj_bb_id
            center = initialize.mid_pts[object_id]
            new_mid_pts[object_id] = center
        initialize.mid_pts = new_mid_pts.copy()
        return obj_boxes_ids



def ad(a, b):
    return a+b