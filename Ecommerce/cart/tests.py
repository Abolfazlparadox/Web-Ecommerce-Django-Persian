# from django.test import TestCase

# # Create your tests here.
# Mostafa Jalili, [12/22/2023 12:56 PM]
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE,default="")
#     name = models.CharField(max_length=250)
#     email = models.CharField(max_length=250,null=True)
#     subject = models.CharField(max_length=250)
#     message = models.TextField()
#     status_comment= models.BooleanField(("staff status"),default=False,null=True)
#     status_comment_reply= models.BooleanField(("staff status"),default=False,null=True)
#     date_created = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now = True)

#     def str(self):
#         return f"{self.name} - {self.post.title} - {self.status_comment}"



# Mostafa Jalili, [12/22/2023 12:56 PM]
# def reply_comment(request, pk = None):
#     resp={'status':'failed', 'msg':'','id':None}
#     if request.method == 'POST':
#         if request.POST['id'] == '':
#             postslug= request.POST ['slug']
#             form = forms.saveComment(request.POST)
            
#         else:
            
#             comment = models.Comment.objects.get(id=request.POST['id'])
#             form = forms.saveComment(request.POST, instance= comment)
            
            
#         if form.is_valid():
#             form.save()
#             if request.POST['id'] == '':
#                 commentID = models.Comment.objects.all().last().id    
#             else:
#                 commentID = request.Comment['id']
                
#             comment_id = request.POST['id_comment']
            

#             resp['status'] = 'success'
#             b = comment_reply(id_comment=commentID, id_comment_reply=comment_id)
#             b.save()
#             messages.success(request, "ریپلای با موفقیت ثبت شد")
            
#         else:
#             for field in form:
#                 for error in field.errors:
#                     if not resp['msg'] == '':
#                         resp['msg'] += str('<br />')
#                     resp['msg'] += str(f"[{field.label}] {error}")

#     else:
#         resp['msg'] = "هیچ اطلاعاتی ارسال نشد"
#     #return HttpResponse(json.dumps(resp), content_type="application/json")
#     return redirect(f'post/{postslug}')