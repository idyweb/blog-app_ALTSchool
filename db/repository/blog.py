from sqlalchemy.orm import Session

from db.models.blog import Blog
from schemas.blog import CreateBlog
from schemas.blog import UpdateBlog


def create_new_blog(blog: CreateBlog, db: Session, author_id, username):
    blog = Blog(**blog.dict(), author_id=author_id, username=username)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def list_blogs(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def retreive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def update_blog(id: int, blog: UpdateBlog, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error": f"Blog with id {id} does not exist"}
    if not blog_in_db.author_id == author_id:  # new
        return {"error": f"Only the author {id} can modify the blog"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db


def delete_blog(id: int, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    if not blog_in_db.first():
        return {"error": f"Could not find blog with id {id}"}
    if not blog_in_db.first().author_id == author_id:  # new
        return {"error": f"Only the author {id} can delete a blog"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"deleted blog with id {id}"}
