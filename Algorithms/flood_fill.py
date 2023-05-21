def floodFill(image, sr, sc, color):
        if image[sr][sc] == color: return image
        start_color = image[sr][sc]
        queue = []
        queue.append([sr,sc])
        image[sr][sc] = color
        while queue:
            # print(image[0])
            # print(image[1])
            # print(image[2])
            current_node = queue.pop()
            sr = current_node[0]
            sc = current_node[1]
            if sr < len(image)-1:
                if image[sr+1][sc] == start_color:
                    image[sr+1][sc] = color
                    queue.append([sr+1,sc])
            if sr > 0:
                if image[sr-1][sc] == start_color:
                    image[sr-1][sc] = color
                    queue.append([sr-1,sc])
            if sc < len(image[0])-1:
                if image[sr][sc+1] == start_color:
                    image[sr][sc+1] = color
                    queue.append([sr,sc+1])
            if sc > 0:
                if image[sr][sc-1] == start_color:
                    image[sr][sc-1] = color
                    queue.append([sr,sc-1])
            print("#######################")
        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))