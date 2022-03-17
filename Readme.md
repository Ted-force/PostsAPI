# PostsAPI
Routes:
1) http://localhost:8000/api/posts/   <br/>
    GET: Get all Posts   <br/>
   2) POST: Create a new Post with title,username and body of Post  <br/>
    (e.g. {
   "title": "New Post",
   "username": "user",
   "body": "New Post Body"
   }) 
   <br />
2) http://localhost:8000/api/posts/id  <br/>
   1)GET: Get Post by ID  <br/>
   2) PUT: Update a Post By ID  <br/>
   DELETE: Delete a post by ID   <br/>
3) http://localhost:8000/api/posts/id/comments/   <br/>
   GET: get all comments for Post with ID   <br/>
   POST: Create a new comment for Post with ID <br />
   (e.g. {
   "username": "user",
   "comment": "new Comment",
   })
   <br/>
4) http://localhost:8000/api/posts/id/comments/id2   <br/>
   GET: get comment by ID2   <br/>
   PUT: update comment with ID2   <br/>
   DELETE: Delete Comment witht ID2 <br />
   
5) http://localhost:8000/api/posts/id/reactions/   <br />
   GET: get all Likes on a post with ID=id   <br />
   
6) http://localhost:8000/api/posts/id/reactions/id2  <br /> 
   POST: Post a new reaction on post with Id=id
    id2 specifies type of reactions
    0=like
    1=Laugh
    2=Amazed
    3=Sad
   (e.g. {
     user: "user2"
     ReactionType: "Like"  //for id2=0
   }
   )
 7)  http://localhost:8000/api/posts/id/reactions/id2/id3 
   DELETE: delete a like with ID=id3 and reactionId=id2 on post with ID=id 
