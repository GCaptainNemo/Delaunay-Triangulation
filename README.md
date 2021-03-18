# Delaunay三角剖分
## 一、介绍
点集的三角剖分(triangulation)，对数值分析(有限元)以及图形学、点云处理来说都是极为重要的一项预处理技术。尤其是Delaunay三角剖分，关于点集的很多几何图都和Delaunay三角剖分相关，
比如Voronoi图等。

## 二、原理
### 2.1 三角剖分定义
假设V是有限点集，e为由点集V中的点作为端点构成的封闭线段，E为e的集合。点集V的三角剖分T = (V, E)就是一张**图**，该图满足条件：
1. 没有相交边
2. 图中所有的面都是三角面，且所有三角面的合集是点集V的凸包(convex hull)。

所谓凸包(convex hull)，就是所有包含点集V的凸集的交，或者形象地说包含点集V的“最小凸多边形”。

### 2.2 Delaunay三角剖分定义
由三角剖分的定义可以看出，点集的三角剖分并不唯一，需要提出额外评价三角剖分好坏的标准。Delaunay三角剖分(Delaunay triangulation, 简称DT)是最常用的三角剖分，
因为它可以避免“尖锐和细长”的三角面片(最大化最小角)。“尖锐和细长”的三角面片在渲染的时候会造成“突变”的视觉效果，在有限元计算时容易因为极端值产生精度损失。下面给出Delaunay三角剖分的定义：

先定义Delaunay边：假设E中的一条边e，若e满足**存在**一个圆经过e的两个端点，**圆内**不含点集V中任何其他的点，这一特性又称为**空圆特性**。

定义Delaunay三角剖分：如果点集V的一个三角剖分T的边集E只包含Delaunay边，则称该三角剖分为Delaunay三角剖分。

### 2.3 Delaunay三角剖分属性
Delaunay三角剖分与Voronoi图是对偶关系，它们之间的性质也有所联系。

1. 空圆性(Empty Circle)：

    a. Delaunay剖分中任何一张三角面的外接圆是空的，即不存在四点共圆或者三角面片三点外接圆内部有其它点的情况。 
    
    ![empty-circla](resources/empty_circle_a.jpg)
    
    b. 在Delaunay三角剖分中，每一条边都存在一个空圆以它为弦(Delaunay边的定义)。
    
    ![empty-circla](resources/empty_circle_b.jpg)
    
    a和b都是空圆性的体现。**注意**：左图是Delaunay三角剖分，右图是对偶图Voronoi图，Voronoi图将区域划分成每个**只包含一个节点**(可以不封闭)，
    且每个区域的点距离该区域顶点最近(垂直平分线连成区域)。
    
2. 最近邻性:任何一条连接于最近邻之间的边都会被Delaunay剖分采用(是Delaunay边)，因为存在一个以该边为直径的空圆，如下图所示。

    ![nearest-neighbour](resources/1nn.jpg)

    按照最近邻关系生成的图又称为最近邻图(Nearest Neighbour Graph, NNG)，它是Delaunay剖分的一个**子图**。NNG是一个有向图，最近邻关系不对等。

3. 复杂度：在二维平面中，每增加一个点三角形数目增加2，边数增加3。在d维空间中，结论是2<sup>d</sup>和3<sup>d</sup>。


## 五、参考资料
[1][百度百科-凸包](https://baike.baidu.com/item/%E5%87%B8%E5%8C%85)

[2][百度百科-Delaunay三角剖分](https://baike.baidu.com/item/Delaunay%E4%B8%89%E8%A7%92%E5%89%96%E5%88%86%E7%AE%97%E6%B3%95/3779918)