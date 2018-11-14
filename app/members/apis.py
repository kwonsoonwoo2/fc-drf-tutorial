from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.serializers import UserSerializer


class AuthTokenView(APIView):
    # URL: '/members/auth-token/'
    def post(self, request):
        # 요청으로부터 username, password를 받음
        # 받은 내용으로 authenticate를 실행
        # - 인증 성공시
        #   인증된 User에 연결되는 Token을 가져오거나 생성(get_or_create)
        #   Token의 key값을 Response에 담아 돌려줌
        # - 인증 실패시
        #   AuthenticationFailed Exception을 raise
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # 인증에 성공하면 토큰을 생성하거나 가져와서 Response에 전달
            token, __ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
            }
            return Response(data)
        raise AuthenticationFailed()


class ProfileView(APIView):
    # URL: '/members/profile/'
    # 인증된 사용자만 접근 가능하도록 permission_classes설정
    permission_classes = (permissions.IsAuthenticated)

    def get(self, request):
        # 현재 요청에 해당하는 User의 정보를
        # UserSerializer로 직렬화 한 후 Response에 보내줌
        return Response(UserSerializer(request.user).data)
