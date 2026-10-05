from blog import Blog
from newsletter import Newsletter
from user import User
from blog_management import BlogManagment
from subscription_type import SubscriptionType 


if __name__ == "__main__":
    blog_management = BlogManagment()
    
    david = User("David")
    tarek = User("Tarek")
    khaled = User("Khaled")
    moustafa = User("Moustafa")

    blog_management.subscribe(SubscriptionType.NEW_BLOG, david)
    blog_management.subscribe(SubscriptionType.NEWSLETTER, david)
    blog_management.subscribe(SubscriptionType.NEWSLETTER, tarek)
    blog_management.subscribe(SubscriptionType.NEW_BLOG, khaled)
    blog_management.subscribe(SubscriptionType.NEW_BLOG, moustafa)

    blog_management.add_new_blog(Blog("My First Blog", "This is my first blog post."))
    blog_management.add_newsletter(Newsletter("Monthly Newsletter", "Stay updated with our latest news."))
