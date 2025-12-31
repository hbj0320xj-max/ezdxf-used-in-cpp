#ifndef CAD_ENGINE_H
#define CAD_ENGINE_H

#ifdef __cplusplus
extern "C" {
#endif

// 基础坐标
typedef struct { double x; double y; } CadPoint;

// 线段
typedef struct { CadPoint start; CadPoint end; } CadLine;

// 圆
typedef struct { CadPoint center; double radius; } CadCircle;

// 圆弧
typedef struct { CadPoint center; double radius; double start_angle; double end_angle; } CadArc;

// 多段线
typedef struct { CadPoint* points; int point_count; int is_closed; } CadPolyline;

// 汇总数据
typedef struct {
    CadLine* lines;      int line_count;
    CadCircle* circles;  int circle_count;
    CadArc* arcs;        int arc_count;
    CadPolyline* polylines; int poly_count;
} CadDrawingData;

// 导出函数
__declspec(dllexport) CadDrawingData* get_cad_data(const char* file_path);
__declspec(dllexport) void free_cad_data(CadDrawingData* data);

#ifdef __cplusplus
}
#endif
#endif