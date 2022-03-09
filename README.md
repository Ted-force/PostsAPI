# PostsAPI
Routes:
1) http://localhost:8000/api/posts/
   GET: Get all Posts
   POST: Create a new Post with title,username and body of Post
2) http://127.0.0.1:8000/api/posts/<int:id>
   GET: Get Post by ID
   PUT: Update a Post By ID
   DELETE: Delete a post by ID
3) http://127.0.0.1:8000/api/posts/<int:id>/comments/ 
   GET: get all comments for Post with ID
   POST: Create a new comment for Post with ID
4) http://127.0.0.1:8000/api/posts/<int:id>/comments/<int:id2>
   GET: get comment by ID
   PUT: update comment with ID
   DELETE: Delete Comment   
   
   


   
  
