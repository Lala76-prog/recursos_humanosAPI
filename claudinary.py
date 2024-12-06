import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dwgrnobbx", 
    api_key = "673153219474924", 
    api_secret = "K2BbSn7wvBSJR7mDYfjnvLt7fHs", # Click 'View API Keys' above to copy your API secret
    secure=True
)

# Upload an image
upload_result = cloudinary.uploader.upload("https://res.cloudinary.com/demo/image/upload/getting-started/empleado.jpg",
                                           public_id="empleado")
print(upload_result["secure_url"])

# Optimize delivery by resizing and applying auto-format and auto-quality
optimize_url, _ = cloudinary_url("empleado", fetch_format="auto", quality="auto")
print(optimize_url)

# Transform the image: auto-crop to square aspect_ratio
auto_crop_url, _ = cloudinary_url("empleado", width=500, height=500, crop="auto", gravity="auto")
print(auto_crop_url)