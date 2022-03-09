# PostsAPI
Routes:
1) http://localhost:8000/api/posts/
   GET: Get all Posts
   POST: Create a new Post with title,username and body of Post
2) http://127.0.0.1:8000/api/posts/id
   GET: Get Post by ID
   PUT: Update a Post By ID
   DELETE: Delete a post by ID
3) http://127.0.0.1:8000/api/posts/id/comments/ 
   GET: get all comments for Post with ID
   POST: Create a new comment for Post with ID
4) http://127.0.0.1:8000/api/posts/id/comments/id2
   GET: get comment by ID2
   PUT: update comment with ID2
   DELETE: Delete Comment witht ID2
