import ezdxf

def analyze_dxf(path):
    try:
        doc = ezdxf.readfile(path)
        msp = doc.modelspace()
        
        # 1. 线
        lines = [((e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)) 
                 for e in msp.query('LINE')]
        
        # 2. 圆
        circles = [((e.dxf.center.x, e.dxf.center.y), e.dxf.radius) 
                   for e in msp.query('CIRCLE')]
        
        # 3. 弧
        arcs = [((e.dxf.center.x, e.dxf.center.y), e.dxf.radius, e.dxf.start_angle, e.dxf.end_angle) 
                for e in msp.query('ARC')]
        
        # 4. 多段线
        polylines = []
        for e in msp.query('LWPOLYLINE'):
            pts = [(p[0], p[1]) for p in e.get_points()]
            polylines.append((pts, 1 if e.closed else 0))
            
        return {
            "lines": lines,
            "circles": circles,
            "arcs": arcs,
            "polylines": polylines
        }
    except Exception as e:
        print(f"Python Error: {e}")
        return None